require 'rspec'
require 'watir-webdriver'
require 'selenium-webdriver'
require 'appium_lib'
require_relative 'yelp'

describe 'Yelp App Installation' do

  before(:each) do
    @cl_instance = Yelp.new
    
    # 'start_session takes two arguments, one is the appPkg name and the other is appActivity name.'
    # 'By default the arguments to start_session is of Yelp'
    @driver = @cl_instance.start_session('com.android.vending', 'com.google.android.finsky.activities.MainActivity')
    @wait_time = @driver.manage.timeouts.implicit_wait = 60
  end

  after(:each) do
    @cl_instance.shut_down
  end

  context 'Installation of App' do

    it 'Should search and install the app', install: true  do

      @child_instance = Installation.new

      # 'By default the item to be searched is Yelp. You can change by providing an app name [Exact Name] of your choice'
      @child_instance.play_store_find

      begin
        button_is = @child_instance.find_id('com.android.vending:id/launch_button')
        text_is = @child_instance.find_id('com.android.vending:id/title_creator').text
        expect(text_is).to eq 'Yelp, Inc'
      rescue
        @child_instance.find_id('com.android.vending:id/buy_button').click
        @child_instance.find_id('com.android.vending:id/continue_button').click
        @wait_time
        @child_instance.find_id('com.android.vending:id/launch_button').click
        tag_line = @child_instance.find_id('com.yelp.android:id/tagline').text
        expect(tag_line).to eq 'Search for nearby restaurants, shops, and services.'
      end
    end

  end


end
