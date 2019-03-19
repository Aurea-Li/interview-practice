require 'httparty'
require_relative 'keys'

#Starter Code:
SEVEN_WONDERS = ["Great Pyramid of Giza", "Hanging Gardens of Babylon", "Colossus of Rhodes", "Pharos of Alexandria", "Statue of Zeus at Olympia", "Temple of Artemis", "Mausoleum at Halicarnassus"]

class CoordinateFinder
  attr_reader :location

  def initialize(location)
    @location = location
  end

  def get_coordinates
    encoded_url = build_url

    response = HTTParty.get(encoded_url)

    return handle_response(response)
  end

  private

  def build_url

    address = @location.split.join('+')
    coordinate_url = "https://maps.googleapis.com/maps/api/geocode/json?address=#{address}&bounds=27.057438, 14.611095|40.948759, 49.189896&key=#{API_KEY}"
    return URI.encode(coordinate_url)

  end

  def handle_response(response)

    if response["status"] == "OK"

      location = response["results"][0]["geometry"]["location"]

      return {
        "lat" => location["lat"],
        "lng" => location["lng"]
        }

    else
      return {
        "lat" => "N/A",
        "lng" => "N/A"
        }
    end
  end
end

coordinate_hash = {}
SEVEN_WONDERS.each do |wonder|


  finder = CoordinateFinder.new(wonder)

  coordinate_hash[finder.location] = finder.get_coordinates


end

puts coordinate_hash



#Example Output:
#{"Great Pyramind of Giza"=>{"lat"=>29.9792345, "lng"=>31.1342019}, "Hanging Gardens of Babylon"=>{"lat"=>32.5422374, "lng"=>44.42103609999999}, "Colossus of Rhodes"=>{"lat"=>36.45106560000001, "lng"=>28.2258333}, "Pharos of Alexandria"=>{"lat"=>38.7904054, "lng"=>-77.040581}, "Statue of Zeus at Olympia"=>{"lat"=>37.6379375, "lng"=>21.6302601}, "Temple of Artemis"=>{"lat"=>37.9498715, "lng"=>27.3633807}, "Mausoleum at Halicarnassus"=>{"lat"=>37.038132, "lng"=>27.4243849}}
