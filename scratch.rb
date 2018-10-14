require 'pry'

def length_of_longest_substring(s)

  substr = {}
  max_length = 0

  s.length.times do |i|
    if substr[s[i]]

      max_length = update_max_length(max_length, substr)


      delete = []
      substr.each do |char, ind|
        if ind < substr[s[i]]
          delete << char
        end
      end

      delete.each do |char|
        substr.delete(char)
      end

    end
    substr[s[i]] = i
  end

  return update_max_length(max_length, substr)
end

def update_max_length(max_length, substr)
  return substr.length > max_length ? substr.length : max_length
end

puts length_of_longest_substring("dvdf")
# puts length_of_longest_substring("aabaab!bb")
# puts length_of_longest_substring("abcabcbb")
# puts length_of_longest_substring("ohvhjdml")
