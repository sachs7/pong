require 'rspec'
require 'appium_lib'

class Testing

  def session

    desired_caps = {
        caps:{
            platformName: 'Android',
            platformVersion: '4.4',
            deviceName: 'XT1063',
            appPackage: 'com.yelp.android',
            appActivity: 'com.yelp.android.ui.activities.RootActivity',
        },
        appium_lib:{
            server_url: 'http://localhost:4723/wd/hub'
        }
    }
    @driver = Appium::Driver.new(desired_caps)
    @driver.start_driver
    Appium.promote_appium_methods Object

  end

  def close
    @driver.driver_quit
  end

  def search(item)
    @driver.find_element(:id, 'com.yelp.android:id/search_text').click
    @driver.find_element(:id, 'com.yelp.android:id/searchbar').send_key(item)
    @driver.find_element(:id, 'com.yelp.android:id/search_button').click
  end

  def scroll_to(text)
    text = %Q("#{text}")
    args = Appium::Android::scroll_uiselector("new UiSelector().text(#{text})")
    find_element :uiautomator, args
  end


end
