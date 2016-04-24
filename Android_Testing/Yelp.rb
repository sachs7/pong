require 'selenium-webdriver'
require 'appium_lib'
require 'CSV'

class Yelp

  # 'Default application is Yelp'
  def start_session(pkg='com.yelp.android', actvty='com.yelp.android.ui.activities.RootActivity')
    
    server_url = 'http://localhost:4723/wd/hub'

    capabilities =
        {
            platformName: 'Android',
            deviceName: 'XT1063',
            appPackage: pkg,
            appActivity: actvty
        }
    @driver = Selenium::WebDriver.for(:remote, :desired_capabilities=>capabilities, :url=>server_url)

    # 'Class Variable to be used in another class'
    @@drive = @driver

  end

  def shut_down
    @driver.quit
  end

  def splash_arrows
    @driver.find_element(:id, 'com.yelp.android:id/next_splash_arrow_button')
  end

  def login_button
    @driver.find_element(:id, 'com.yelp.android:id/login_button')
  end

  # 'Login with invalid credentials'
  def user_data(filename)
    user_data = CSV.read Dir.pwd + filename
    descriptor = user_data.shift
    descriptor = descriptor.map { |key| key.to_sym }
    user_data.map { |user| Hash[ descriptor.zip(user) ] }
  end

  def notification_text
    @driver.find_element(:id, 'android:id/message').text
  end

  def username
    @driver.find_element(:id, 'com.yelp.android:id/activity_login_editUsername')
  end

  def password
    @driver.find_element(:id, 'com.yelp.android:id/activity_login_editPassword')
  end

  def sign_up
    @driver.find_element(:id, 'com.yelp.android:id/sign_up_button')
  end

  # 'Search box'
  def search_for(item)
    @driver.find_element(:id, 'com.yelp.android:id/search_text').click
    @driver.find_element(:id, 'com.yelp.android:id/searchbar').send_key(item)
  end

  def search_button
    @driver.find_element(:id, 'com.yelp.android:id/search_button').click
  end

  # 'find element by name and click'
  def find_name(name)
    @driver.find_element(:name, name).click
  end

  # 'find element by id'
  def find_by_id(item)
    @driver.find_element(:id, item)
  end

  # 'find element by class'
  def find_class(item)
    @driver.find_element(:class, item)
  end

  # 'Sign up with missing items'
  def sign_up_users(first_name, last_name, email, password)
    find_by_id('com.yelp.android:id/first_name').send_key first_name
    find_by_id('com.yelp.android:id/last_name').send_key last_name
    find_by_id('com.yelp.android:id/email_address').send_key email
    find_by_id('com.yelp.android:id/password').send_key password
    find_name('Gender')
    find_name('Male')
  end

  def login_success(user_name, pass_word)
    find_class('android.widget.ImageButton').click
    find_by_id('com.yelp.android:id/nav_sign_up_log_in_button').click
    username.send_key(user_name)
    password.send_key(pass_word)
    find_by_id('com.yelp.android:id/activity_login_btnLogin').click
    find_class('android.widget.ImageButton').click
    u_name = find_by_id('com.yelp.android:id/nav_user_name').text
  end
  
  def login_after_install(uname, pword)
    splash_arrows.click
    splash_arrows.click
    login_button.click
    username.send_key(uname)
    password.send_key(pword)
    find_by_id('com.yelp.android:id/activity_login_btnLogin').click
    notification_text
  end


end

class Installation < Yelp

  # 'In Play Store find the item. (Default item is Yelp)'
  def play_store_find(item='Yelp')
    @@drive.find_element(:class, 'android.widget.FrameLayout').find_element(:id, 'com.android.vending:id/action_bar_container_container').find_element(:id, 'com.android.vending:id/text_container').send_key(item)
    @@drive.find_element(:id, 'com.android.vending:id/suggestion_list_recycler_view').find_element(:id, 'com.android.vending:id/suggest_text').click
  end

  def find_id(id_is)
    @@drive.find_element(:id, id_is)
  end


end
