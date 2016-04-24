require 'rspec'
require 'selenium-webdriver'
require 'appium_lib'
require 'CSV'
require_relative 'yelp'

describe 'Yelp Login and Sign Up Automation' do

  before(:each) do
    @cls_instance = Yelp.new
    @app_driver = @cls_instance.start_session
    @app_driver.manage.timeouts.implicit_wait = 25
  end

  after(:each) do
    @cls_instance.shut_down
  end

  context 'Login text' do

    it 'Should Check for Log In text', login_text: true do
      begin
        @cls_instance.splash_arrows.click
        @cls_instance.splash_arrows.click
        @cls_instance.login_button.click
        txt = @cls_instance.find_class('android.widget.TextView').text
        expect(txt).to eq 'Log In'
      rescue Exception => error
        p error.message
      end
    end

  end

  context 'Check for invalid credentials' do

    it 'Should throw error', invalid_credentials: true do
      @cls_instance.splash_arrows.click
      @cls_instance.splash_arrows.click
      @cls_instance.login_button.click

      @cls_instance.user_data('/user_data.csv').each do |user|
        begin
          @cls_instance.username.send_key user[:username]
          @cls_instance.password.send_key user[:password]
          @cls_instance.find_by_id('com.yelp.android:id/activity_login_btnLogin').click

          begin
            if @cls_instance.notification_text == 'Wrong email or password.'
              @cls_instance.find_by_id('android:id/button2').click
            elsif @cls_instance.notification_text == 'Please enter your email address.'
              @cls_instance.find_by_id('android:id/button3').click
            elsif @cls_instance.notification_text == 'Please enter your password.'
              @cls_instance.find_by_id('android:id/button3').click
            end
          rescue Exception => error
            puts error.message
          end
        rescue Exception => error
          p error.message
        end
      end
    end

  end

  context 'Forgot Password' do

    it 'Display proper message', forgot_password: true do
      @cls_instance.splash_arrows.click
      @cls_instance.splash_arrows.click
      @cls_instance.login_button.click
      @cls_instance.username.send_key('up.sachi@gmail.com')
      @cls_instance.password.send_key('HelloWorld!')
      @cls_instance.find_by_id('com.yelp.android:id/activity_login_btnLogin').click
      begin
        if @cls_instance.notification_text == 'Wrong email or password.'
          @cls_instance.find_by_id('android:id/button1').click
          expect(@cls_instance.notification_text).to eq 'No problem! We\'ve emailed you with instructions on how to reset your password'
        end
      rescue Exception => error
        p error.message
      end
    end

  end

  context 'Sign Up text' do

    it 'Should have a sign up for yelp text', signup_text: true do
      @cls_instance.splash_arrows.click
      @cls_instance.splash_arrows.click
      @cls_instance.sign_up.click
      text_is = @cls_instance.find_class('android.widget.TextView').text
      expect(text_is).to eq 'Sign Up for Yelp'
    end

    it 'Should give missing information error', missing_signup_text: true do
      @cls_instance.splash_arrows.click
      @cls_instance.splash_arrows.click
      @cls_instance.sign_up.click

      @cls_instance.user_data('/sign_up_missing_data.csv').each do |user|
        begin
          @cls_instance.sign_up_users(user[:first_name], user[:last_name], user[:email_address], user[:password])
          @cls_instance.find_by_id('com.yelp.android:id/signup_button').click
          begin
            if @cls_instance.notification_text == 'Please enter your first name.'
              @cls_instance.find_by_id('android:id/button3').click
            elsif @cls_instance.notification_text == 'Please enter your last name.'
              @cls_instance.find_by_id('android:id/button3').click
            elsif @cls_instance.notification_text == 'This email address is invalid.'
              @cls_instance.find_by_id('android:id/button3').click
            end
          rescue Exception => error
            puts error.message
          end
        rescue Exception => error
          p error.message
        end
      end
    end

  end

  context 'Skip sign up' do

    it 'Should be taken to ', skip_signup: true do
      begin
        @cls_instance.splash_arrows.click
        @cls_instance.splash_arrows.click
        @cls_instance.sign_up.click
        @cls_instance.find_by_id('com.yelp.android:id/skip').click
      rescue
        title_text = @cls_instance.find_by_id('com.yelp.android:id/title').text
        expect(title_text).to eq 'Restaurants'
      rescue Exception => error
        p error.message
      end
    end

  end

  context 'Login' do

    it 'Should Login Successfully', login: true do
      begin
        u_name = @cls_instance.login_success(<Your username>, <Your password>)
        expect(u_name).to eq <Your name>
      rescue
        verify_text = @cls_instance.login_after_install(<Your username>, <Your password>)
        expect(verify_text).to eq 'Great! Now you can add reviews, upload photos, check in and bookmark your favorite businesses!'
      rescue Exception => error
        p error.message
      end
    end
    
  end

end

