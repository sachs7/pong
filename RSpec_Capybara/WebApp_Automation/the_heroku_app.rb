require 'capybara/poltergeist'
require 'rest-client'

class The_Heroku_App
  def start_browser
    #@session = Capybara::Session.new (:selenium)
    @session = Capybara.current_session
    #@session = Capybara::Session.new(:poltergeist)
  end

  def tear_down
    @session.execute_script('window.close();')
  end

  def go_to(site)
    @session.visit site
  end

  def click_on_link(name)
    @session.click_link name
  end

  def checkbox_clicked?
    @session.find(:css, 'input:nth-child(1)[type="checkbox"]').checked?
  end

  def click_checkbox
    @session.find(:css, 'input:nth-child(1)[type="checkbox"]').click
  end

  def clear_checkbox
    @session.find(:css, 'input:nth-child(1)[type="checkbox"]').clear
  end

  def drag_and_drop_script
    dnd_javascript = File.read('C:\Users\Sachi\Desktop\287\Sachin_Test_Automation' + '\dnd.js')
    dnd_javascript+"$('#column-a').simulateDragDrop({ dropTarget: '#column-b'});"
  end

  def by_id(name)
    @session.find_by_id(name)
  end

  def find_all_drop_down
    #@session.select(option, from: 'dropdown')
    @session.find('#dropdown').all('option').collect(&:text)
  end

  def select_dropdown(x)
    @session.select(x, from: 'dropdown')
  end

  def switch_frames(parent, child)
    @session.within_frame(parent){@session.within_frame(child){@session.text}}
  end

  def single_frame(parent)
    @session.within_frame(parent){@session.text}
  end

  def is_image_ok?
    all_images = @session.all(:css, 'img')
    status_code = []
    all_images.each do |img|
      RestClient.get img[:src] do |response|
        status_code << response.code
      end
    end
    status_code
  end

  def check_redirected_links
    status_links = []
    all_links = @session.all(:css, 'a')
    all_links.each do |a|
      #p a[:href]
      status_links.push(a[:href])
    end
    len = status_links.size
    new_links = status_links[1...len-1]
    #p new_links
    status_codes = []
    new_links.each do |x|
      #p x
      RestClient.get x do |response|
        status_codes.push(response.code)
      end
    end
    status_codes
  end

  def check_file_download
    ln = @session.all(:css, 'a')
    ln_result = []
    ln.each do |l|
      ln_result.push(l[:href])
    end
    length_of_ar = ln_result.size
    linkers = ln_result[1...length_of_ar-1]
    responses = ''
    linkers.each do |tes|
      #p tes
      responses = RestClient.head(tes)
    end
    responses
  end

  # This is for Example 1 Table
  def check_sorted_table_without_class(sort_type, column_name)
    if sort_type == 'asc'
      @session.find(:css, '#table1 thead tr th:nth-of-type('+column_name.to_s+')').click
    elsif sort_type == 'desc'
      @session.find(:css, '#table1 thead tr th:nth-of-type('+column_name.to_s+')').click
      @session.find(:css, '#table1 thead tr th:nth-of-type('+column_name.to_s+')').click
    else
      raise 'Error: Only asc and desc are supported'
    end
    dues_desc = @session.all(:css, '#table1 tbody tr td:nth-of-type('+column_name.to_s+')')
    due_values_desc = ''
    dues_desc.each do |x|
      if x.text.include? '$'
        due_values_desc = dues_desc.map{|x| x.text.delete('$').to_f}
      else
        due_values_desc = dues_desc.map{|x| x.text}
      end
    end
    due_values_desc
  end

  # This is for Example 2 Table
  def check_sorted_table_with_class(sort_type, column_name)
    if sort_type == 'asc'
      @session.find(:css, '#table2 thead .'+column_name+'').click
    elsif sort_type == 'desc'
      @session.find(:css, '#table2 thead .'+column_name+'').click
      @session.find(:css, '#table2 thead .'+column_name+'').click
    else
      raise 'Error: Only asc and desc are supported'
    end
    dues_desc = @session.all(:css, '#table2 tbody .'+column_name+'')
    due_values_desc = ''
    dues_desc.each do |x|
      if x.text.include? '$'
        due_values_desc = dues_desc.map{|x| x.text.delete('$').to_f}
      else
        due_values_desc = dues_desc.map{|x| x.text}
      end
    end
    due_values_desc
  end

end
