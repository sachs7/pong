require 'rspec'
require 'capybara'
require 'capybara/rspec/features'

session = Capybara::Session.new(:selenium)

feature 'Click on a link in GitHub page' do
  scenario 'User clicks Explore link' do
    session.visit 'http://github.com'
    session.click_link 'Explore'
    expect(session).to have_content('GitHub')
  end
end

feature 'Goto google home page' do
  scenario 'search for ruby' do
    session.visit('http://google.com')
    session.fill_in('q', with: 'ruby')
    expect(session).to have_content('ruby')
  end
end


