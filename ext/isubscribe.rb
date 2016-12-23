#!/usr/bin/env ruby
#
# Sensu - iSubscribe Event Handler
#
# This handler takes events and POSTs them to a iSubscribe events URI.
#
# For configuration see: isubscribe_event.json
#

# Author: Itamar Lavender <itamar.lavender@gmail.com>
#


require 'sensu-handler'
require 'net/http'
require 'net/https'
require 'uri'
require 'json'

class Isubscribe < Sensu::Handler
  def post_event(uri, params)
    uri          = URI.parse(uri)
    req          = Net::HTTP::Post.new(uri.path)
    sock         = Net::HTTP.new(uri.host, uri.port)
    sock.use_ssl = uri.scheme == 'https' ? true : false

    req.basic_auth(uri.user, uri.password) if uri.user
    req.set_form_data(params)

    sock.start { |http| http.request(req) }
  end

  def handle

    uri = settings['isubscribe']['server_uri']

    params = {
      'entity' => @event['client']['name'] + ':' + @event['check']['name'],
      'status' => @event['check']['status'],
      'output' => @event['check']['output'],
      'history' => @event['check']['history'],        
      'occurrences' => @event['occurrences'],
      'timestamp' => Time.now.to_i,
      'api_token' => settings['isubscribe']['api_token']
    }    

    begin
      post_event(uri, params)
    rescue => e
      bail "failed to send event to #{uri}: #{e}"
    end
      puts "sent event to isubscribe: #{params.to_json}"
  end    
end