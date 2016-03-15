require 'rspec'
require 'zombie'

describe Zombie do

  before(:each) do
    @class_instance = Zombie.new
  end

  context 'check name and wish_me' do
    #it 'is named zom', :slow => true do
    it 'is named zom', slow: true do
      #zombie = Zombie.new
      #expect(zombie.name).to eq('Ash')
      #expect(zombie.age).to eql 2
      #sleep 20
      expect(@class_instance.name).to eq 'zom'
      expect(@class_instance.age).to eq 2
    end

    it 'Tell Zombie to wish_me' do
      #zombie = Zombie.new
      #msg = zombie.wish_me('Ron')
      #expect(msg).to eq('Hello Ron')
      msg = @class_instance.wish_me('Ron')
      expect(msg).to eq 'Hello Ron'
    end
  end

  context 'check if string has vowels' do
    it 'should have vowels' do
      #g = Zombie.new
      #expect(g.am_i_vowel?('Testing')).to be true
      expect(@class_instance.am_i_vowel?('Testing')).to be true
    end

    it 'Should not have VOWELS' do
      #g = Zombie.new
      #expect(g.am_i_vowel?('tyrp')).to be false
      expect(@class_instance.am_i_vowel?('typ')).to be false
    end
  end

  context 'Check if a number is greater than 10' do
    it 'The number should be grater than 10' do
      #number = Zombie.new
      #expect(number.am_i_greater?(5)).to be false
      expect(@class_instance.am_i_greater?(5)).to be false
    end
  end
end
