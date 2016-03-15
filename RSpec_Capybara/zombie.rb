class Zombie
  attr_accessor :name, :age, :str, :num

  def initialize
    puts "\n New instance of Zombie..."
    @name = "zom"
    @age = 2
  end

  def wish_me(tes)
    "Hello #{tes}"
  end

  def am_i_vowel?(str)
    !!(str =~ /[aeiou]+/i)
  end

  def am_i_greater?(num)
    num > 10 ? true:false
  end
end
