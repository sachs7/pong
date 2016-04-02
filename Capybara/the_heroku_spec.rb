require 'rspec'
require 'capybara'
require 'C:\Users\Sachi\Desktop\287\Sachin_Test_Automation\the_heroku_app.rb'

RSpec.configure do |c|
  c.filter_run_excluding valid: true
  c.filter_run_excluding invalid: true
end

describe 'Verifying the components of the_heroku_app' do

  before(:each) do
    @cls_instance = The_Heroku_App.new
    @browser = @cls_instance.start_browser
    @cls_instance.go_to 'https://the-internet.herokuapp.com'
  end

  after(:each) do
    @cls_instance.tear_down
  end

  context 'Title and Body' do

    it 'Check for title of the page', page_title: true  do
      expect(@browser.title).to eq('The Internet')
    end

    it 'Check for the body of page', page_body: true  do
      expect(@browser).to have_content('Welcome to the Internet')
    end

  end

  context 'Checkbox' do

    it 'Verification of Checkbox', chk_box: true  do
      expect(@browser).to have_content('Welcome')
      @cls_instance.click_on_link 'Checkboxes'
      checkbox_1 = @cls_instance.checkbox_clicked?

      if !checkbox_1
        @cls_instance.click_checkbox
        expect(@cls_instance.checkbox_clicked?).to eq TRUE
      else
        @cls_instance.clear_checkbox
        expect(@cls_instance.checkbox_clicked?).to eq FALSE
      end
    end

  end

  context 'Credentials' do

    it 'Verify Basic Auth with VALID credentials', valid: true do
      @cls_instance.click_on_link 'Basic Auth'
      @browser.visit 'http://admin:admin@the-internet.herokuapp.com/basic_auth'
      expect(@browser).to have_content 'Congratulations! You must have the proper credentials.'
    end

    it 'Verify Basic Auth with INVALID credentials', invalid: true  do
      @cls_instance.click_on_link 'Basic Auth'
      #@browser.visit 'http://admin:123@the-internet.herokuapp.com/basic_auth'
      statuss = system('authentication.exe')
      puts statuss
      expect(@browser).to have_content 'Not authorized'
    end

  end

  context 'Drag and Drop' do

    it 'Should drag and drop Column A to Column B', dnd: true  do
      @cls_instance.click_on_link 'Drag and Drop'
      @browser.execute_script(@cls_instance.drag_and_drop_script)
      expect(@cls_instance.by_id('column-a').text).to eq 'B'
      expect(@cls_instance.by_id('column-b').text).to eq 'A'
    end

  end

  context 'Dropdown box/Select box' do

    #it 'Should select option 1', drop_down: true do
    #  @cls_instance.click_on_link 'Dropdown'
    #  status = @cls_instance.drop_down 'Option 1'
    #  expect(status).to eq 'ok'
    #end

    #it 'Should select option 2', drop_down: true do
    #  @cls_instance.click_on_link 'Dropdown'
    #  status = @cls_instance.drop_down 'Option 2'
    #  expect(status).to eq 'ok'
    #end

    it 'Should select all options', drop_down: true  do
      @cls_instance.click_on_link 'Dropdown'
      values = @cls_instance.find_all_drop_down
      nw_vals = values[1..values.length]
      #results = [] #ff
      #nw_vals.each {|x| results << @cls_instance.select_dropdown(x) == 'ok' ? true: false}#ff
      #results.each{|x| expect(x).to eq 'ok'}#ff
      nw_vals.each{|x| @cls_instance.select_dropdown(x)}
    end

  end


end
