require 'rspec'
require 'appium_lib'
require 'selenium-webdriver'
require_relative 'testing'


describe 'testing' do

  before(:each) do
    @instance = Testing.new
    @instance.session
    sleep(30)
  end

  after(:each) do
    @instance.close
  end

  context 'Category Search' do

    it 'Should launch Food category', food_section: true do
      begin
        find_element(:name, 'More Categories').click
        @instance.scroll_to('Food').click
        tex = find_element(:class, 'android.widget.TextView').text
        p tex
        expect(tex).to eq 'Food'
      rescue Exception => error
        p error.message
      end
    end

    it 'Search for Review', review: true do
      begin
        @instance.search('bbq')
        wait {find_element(:name, '2. SmokeEaters').click}
        res = wait_true { ! exists { find_exact 'Recommended Reviews' } }
        expect(res).to eq true
      rescue Exception => error
        p error.message
      end
    end

  end


end
