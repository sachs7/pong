require 'rspec'
require 'selenium-webdriver'
require 'appium_lib'
require 'CSV'
require_relative 'yelp'

# 'Give the tag name of the test cases which you don't want to run'
RSpec.configure do |c|
  c.filter_run_excluding valid_search: false
  c.filter_run_excluding invalid_search: false
  c.filter_run_excluding local_address: false
  c.filter_run_excluding suggestion: false
  c.filter_run_excluding click_more: false
end

describe 'Yelp - Basic testing' do

  before(:each) do
    @cls_instance = Yelp.new
    @app_driver = @cls_instance.start_session
    @app_driver.manage.timeouts.implicit_wait = 20
  end

  after(:each) do
    @cls_instance.shut_down
  end

  context 'Yelp - Search bar' do

    it 'Should give proper search results', valid_search: true do
      @cls_instance.search_for('Starbucks')
      result = @app_driver.find_elements(:name, '1. Starbucks')
      result.each do |x|
        expect(x.text).to eq '1. Starbucks'
      end
    end

    it 'Should show search results wrt., current address', local_address: true do
      @cls_instance.search_for('Starbucks')
      @cls_instance.search_button
      result = @app_driver.find_elements(:name, 'com.yelp.android:id/search_address1_textview')
      result.each do |x|
        expect(x.text).to eq '101 E Santa Clara St, Downtown'
      end
    end

    it 'Should say no results found', invalid_search: true do
      @cls_instance.search_for('adskhfvjdflk')
      @cls_instance.search_button
      error_result = @cls_instance.find_by_id('com.yelp.android:id/error_text').text
      expect(error_result).to eq 'No results found!'
    end

    it 'Suggestion box displayed', suggestion: true do
      @cls_instance.search_for('ta')
      suggestion_result = @app_driver.find_elements(:id, 'com.yelp.android:id/term')
      s_result = []
      suggestion_result.each do |x|
        p x.text
        s_result.push(x.text)
      end
      expect(s_result.include? 'tacos').to eq true
      expect(s_result.include? 'Taxis').to eq true
    end

  end

  context 'More Categories' do

    it 'Click on More Categories', click_more: true do
      @cls_instance.find_name('More Categories')
      el = @app_driver.find_element(:id, 'com.yelp.android:id/toolbar').find_element(:class, 'android.widget.TextView')
      expect(el.text).to eq 'More Categories'
    end

  end


end
