class The_Heroku_App

  def start_browser
    @session = Capybara::Session.new (:selenium)
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

end
