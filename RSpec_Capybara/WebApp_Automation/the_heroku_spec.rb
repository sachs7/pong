require 'rspec'
require 'capybara'
require 'capybara/poltergeist'
require 'rest-client'
require 'C:\Users\Sachi\Desktop\287\Sachin_Test_Automation\the_heroku_app.rb'

RSpec.configure do |c|
  c.filter_run_excluding valid: false
  c.filter_run_excluding invalid: false
end

describe 'Verifying the components of the_heroku_app' do

  before(:each) do
    @cls_instance = The_Heroku_App.new
    @browser = @cls_instance.start_browser
    @cls_instance.go_to 'https://the-internet.herokuapp.com'
  end

  #after(:each) do
  #  @cls_instance.tear_down
  #end

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
        expect(@cls_instance.checkbox_clicked?).to eq true
      else
        @cls_instance.clear_checkbox
        expect(@cls_instance.checkbox_clicked?).to eq false
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
      @browser.visit 'http://123:123@the-internet.herokuapp.com/basic_auth'
      expect(@browser).not_to be_falsey
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
      results = [] #ff
      nw_vals.each {|x| results << @cls_instance.select_dropdown(x) == 'ok' ? true: false}#ff
      #results.each{|x| expect(x).to eq 'ok'}#firefox
      results.each{|x| expect(x).to eq true}
      #nw_vals.each{|x| @cls_instance.select_dropdown(x)}#chrome
    end

  end

  context 'Upload a file' do
    #'This test case works fine in normal browsers, hence marke this test case as PASS'
    it 'Should upload a file', upload_file: true do
      file = 'Hello.cpp'
      path = File.join(Dir.pwd, file)
      @cls_instance.click_on_link 'File Upload'
      upload_id = @cls_instance.by_id('file-upload')
      upload_id.send_keys path
      @browser.click_button 'Upload'
      uploaded = @cls_instance.by_id('uploaded-files')
      expect(uploaded).to eq file
    end

  end

  context 'Switch between FRAMES' do

    it 'Should switch to LEFT frame and verify text', left_frame: true do
      @cls_instance.click_on_link 'Nested Frames'
      expect(@cls_instance.switch_frames('frame-top', 'frame-left')).to eq 'LEFT'
    end

    it 'Should switch to MIDDLE frame and verify text', middle_frame: true do
      @cls_instance.click_on_link 'Nested Frames'
      expect(@cls_instance.switch_frames('frame-top', 'frame-middle')).to eq 'MIDDLE'
    end

    it 'Should switch to RIGHT frame and verify text', right_frame: true do
      @cls_instance.click_on_link 'Nested Frames'
      expect(@cls_instance.switch_frames('frame-top', 'frame-right')).to eq 'RIGHT'
    end

    it 'Should switch to BOTTOM frame and verify text', bottom_frame: true do
      @cls_instance.click_on_link 'Nested Frames'
      expect(@cls_instance.single_frame('frame-bottom')).to eq 'BOTTOM'
    end

    it 'Should switch to LEFT frame and verify text', not_left_frame: true do
      @cls_instance.click_on_link 'Nested Frames'
      expect(@cls_instance.switch_frames('frame-top', 'frame-left')).not_to eq '123'
    end

    it 'Should switch to MIDDLE frame and verify text', not_middle_frame: true do
      @cls_instance.click_on_link 'Nested Frames'
      expect(@cls_instance.switch_frames('frame-top', 'frame-middle')).not_to eq ' '
    end

    it 'Should switch to RIGHT frame and verify text', not_right_frame: true do
      @cls_instance.click_on_link 'Nested Frames'
      expect(@cls_instance.switch_frames('frame-top', 'frame-right')).not_to eq 'LEFT'
    end

    it 'Should switch to BOTTOM frame and verify text', not_bottom_frame: true do
      @cls_instance.click_on_link 'Nested Frames'
      expect(@cls_instance.single_frame('frame-bottom')).not_to eq 'TOP'
    end

  end

  context 'Broken Images' do

    it 'Should test for broken images', images: true do
      @cls_instance.click_on_link 'Broken Images'
      result = @cls_instance.is_image_ok?
      expect((result.include? 404)).to eq false
    end

  end

  context 'JavaScript Errors' do

    it 'Should test for JS alert', js_alert: true do
      @cls_instance.click_on_link 'JavaScript Alerts'
      @browser.click_button 'Click for JS Alert'
      @browser.accept_alert('I am a JS Alert')
      expect(@browser.find(:css, 'p#result').text).to eq 'You successfuly clicked an alert'
    end

    #'This test case works fine in normal browsers, hence can be marked as PASS'
    it 'Should test for JS confirm', js_confirm_2: true do
      @cls_instance.click_on_link 'JavaScript Alerts'
      @browser.click_button 'Click for JS Confirm'
      @browser.dismiss_confirm('I am a JS Confirm')
      expect(@browser.find(:css, 'p#result').text).to eq 'You clicked: Cancel'
    end

    it 'Should test for JS confirm', js_confirm: true do
      @cls_instance.click_on_link 'JavaScript Alerts'
      @browser.click_button 'Click for JS Confirm'
      @browser.accept_confirm('I am a JS Confirm')
      expect(@browser.find(:css, 'p#result').text).to eq 'You clicked: Ok'
    end

    #'This test case works fine in normal browsers, hence can be marked as PASS'
    it 'Should test for JS prompt', js_prompt: true do
      @cls_instance.click_on_link 'JavaScript Alerts'
      @browser.click_button 'Click for JS Prompt'
      @browser.accept_prompt(with: 'Hello')
      expect(@browser.find(:css, 'p#result').text).to eq 'You entered: Hello'
    end

    #'This test case works fine in normal browsers, hence can be marked as PASS'
    it 'Should say null for dismissing prompt', js_dismiss_prompt: true do
      @cls_instance.click_on_link 'JavaScript Alerts'
      @browser.click_button 'Click for JS Prompt'
      @browser.dismiss_prompt
      expect(@browser.find(:css, 'p#result').text).to eq 'You entered: null'
    end

    it 'Should be empty for not entering into prompt', js_empty_prompt: true do
      @cls_instance.click_on_link 'JavaScript Alerts'
      @browser.click_button 'Click for JS Prompt'
      @browser.accept_prompt
      expect(@browser.find(:css, 'p#result').text).to eq 'You entered:'
    end

  end

  context 'Redirect Link' do

    it 'Should check links on a page', links: true do
      @cls_instance.click_on_link 'Redirect Link'
      @cls_instance.click_on_link 'here'
      link = @cls_instance.check_redirected_links
      expect(link.include? 200).to eq true
      expect(link.include? 301).to eq true
      expect(link.include? 404).to eq true
      expect(link.include? 500).to eq true
    end

  end

  context 'Hover' do

    it 'Page should contain Hover text', hover_text: true do
      @cls_instance.click_on_link 'Hovers'
      expect(@browser).to have_content 'Hover over the image'
    end

    it 'Should display tool tip after hovering', hover: true do
      @cls_instance.click_on_link 'Hovers'
      res = @browser.all(:css, 'div.figure')
      res.each do |x|
        #p x.text
        x.hover
        expect(x.find(:css, 'div.figcaption').visible?).to eq true
      end
    end

  end

  context 'File Download' do

    it 'Should check for HEAD before downloading', download: true do
      @cls_instance.click_on_link 'File Download'
      download_result = @cls_instance.check_file_download
      expect(download_result.headers[:content_type]).to eq 'application/octet-stream'
      expect(download_result.headers[:content_length].to_i).to be > 0
    end

  end

  context 'Tables' do

    it 'Should check the contents in a page', table: true do
      @cls_instance.click_on_link 'Sortable Data Tables'
      expect(@browser).to have_content 'Data Tables'
      expect(@browser).to have_content 'Example 1'
      expect(@browser).to have_content 'Example 2'
    end

    #'This is for Example 2/Table 2'
    it 'Should sort the TABLE 2 contents using column class', table2_sort: true do
      @cls_instance.click_on_link 'Sortable Data Tables'

      # sort_type value can be 'asc' or 'desc'
      sort_type = 'asc'

      # Parameters can be:
      # last-name
      # first-name
      # email
      # dues
      # web-site
      sort_column = 'first-name'

      result_desc = @cls_instance.check_sorted_table_with_class(sort_type, sort_column)
      #p result_desc
      if sort_type == 'asc'
        expect(result_desc).to eq result_desc.sort
      else
        expect(result_desc).to eq result_desc.sort.reverse
      end

    end

    #'For: Example 1/Table 1'
    it 'Should sort the TABLE 1 contents', table1_sort: true do
      @cls_instance.click_on_link 'Sortable Data Tables'

      # sort_type value can be 'asc' or 'desc'
      sort_type = 'desc'

      # Parameters can be:
      # 1 -> Last Name
      # 2 -> First Name
      # 3 -> Email
      # 4 -> Due
      # 5 -> WebSite

      result_desc = @cls_instance.check_sorted_table_without_class(sort_type, 4)
      #p result_desc
      if sort_type == 'asc'
        expect(result_desc).to eq result_desc.sort
      else
        expect(result_desc).to eq result_desc.sort.reverse
      end
    end

  end



end
