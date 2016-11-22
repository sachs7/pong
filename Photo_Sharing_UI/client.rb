require 'gtk3'
require 'curb'
require 'rest_client'
require 'nokogiri'
require 'open-uri'
require 'double_bag_ftps'
require 'typhoeus'

class RubyApp < Gtk::Window

    def initialize
        super
		@url; @snd; @snd1; @snd2; @tes; @summary; @usernme; @passuser; @result; @newuser; @newpasswd; @signpage; @chk
		@chk1 # this is for empty entries 
		@cmpre
		@result1  #this is for chking if user already exists.
		@success  #upload successful
		@fail	  #upload not successful	
		#@conn #-------Testing for summary
		@folder_server_contents; @folder_details
		@ftps #--------------------ftp testing
		@testing; @testingserver; @dwnload; @res_file_dwnload; @success_download; @fail_download
        init_ui
    end
    
    def init_ui
	  begin	
        	fixed = Gtk::Fixed.new
        	add fixed
		
		header = Gtk::Label.new "Welcome to Ruby File upload GUI."
		fixed.put header, 10, 10
		
		login_header = Gtk::Label.new "Login Details."
		fixed.put login_header, 600, 10
		
		user_name = Gtk::Label.new "Username: "
		fixed.put user_name, 510, 80
		
		userentry = Gtk::Entry.new
		fixed.put userentry, 580, 80

		userentry.signal_connect "key-release-event" do |u, ev|
			user_key_release u, ev
		end
		
		pass_name = Gtk::Label.new "Password: "
		fixed.put pass_name, 510, 130
		
		passentry = Gtk::Entry.new
		passentry.visibility=false                # To Mask the password
		fixed.put passentry, 580, 130
		
		passentry.signal_connect "key-release-event" do |p, eve|
			pass_key_release p, eve
		end
		
		label = Gtk::Label.new "URL"
        	fixed.put label, 10, 60
		
		urlentry = Gtk::Entry.new
        	fixed.put urlentry, 60, 60
		
		urlentry.signal_connect "key-release-event" do |s, ev|
			url_key_release s, ev
		end
		
		entry = Gtk::Entry.new
        	fixed.put entry, 60, 120

        	entry.signal_connect "key-release-event" do |w, e|
			on_key_release w, e
        	end
		
		entry1 = Gtk::Entry.new
        	fixed.put entry1, 60, 170

        	entry1.signal_connect "key-release-event" do |w1, e1|
			on_key_release1 w1, e1
        	end
		
		entry2 = Gtk::Entry.new
        	fixed.put entry2, 60, 220

        	entry2.signal_connect "key-release-event" do |w2, e2|
			on_key_release2 w2, e2
        	end
		
		button = Gtk::Button.new :label => "Upload"   
        	button.signal_connect "clicked" do 
		if @chk
			transfer(@url, @snd)
		else
			on_error_login
		end
			msg(@url)
		end
		
		button1 = Gtk::Button.new :label => "Upload"   
        	button1.signal_connect "clicked" do 
		if @chk
			transfer(@url, @snd1)
		else
			on_error_login
		end
			msg(@url)
		end

        	button2 = Gtk::Button.new :label => "Upload"   
        	button2.signal_connect "clicked" do 
			if @chk
				transfer(@url, @snd2)
			else
				on_error_login
			end
			msg(@url)
		end
		
		button3 = Gtk::Button.new :label => "Login"   
        	button3.signal_connect "clicked" do 
			login(@usernme, @passuser)
		end
		
		button4 = Gtk::Button.new :label => "Sign Up"   
        	button4.signal_connect "clicked" do 
			signup(@usernme, @passuser)
		end
		
		# Button to view the contents of the Server Directory
		view_header = Gtk::Label.new "View the contents of the Server Directory."
		fixed.put view_header, 10, 300
		
		button5 = Gtk::Button.new :label => "View"
		button5.signal_connect "clicked" do
			if @chk
				view_files
			else
				on_error_login
			end
			msg(@url)
		end
		
		warning = Gtk::Label.new "Warning* : Only the files uploaded by PARTNER Servers can be downloaded."
		fixed.put warning, 490, 380
		
		download_header = Gtk::Label.new "To Download a file, please enter the file name along with its extension.*"
		fixed.put download_header, 10, 350
		
		download_text = Gtk::Entry.new
        	fixed.put download_text, 60, 370

        	download_text.signal_connect "key-release-event" do |w3, e3|
			on_download_pressed w3, e3
        	end
		
		button6 = Gtk::Button.new :label => "Download"
		button6.signal_connect "clicked" do
			if @chk
				download_server_files(@dwnload)
			else
				on_error_login
			end
			msg(@url)
		end

        	fixed.put button, 240, 120
		fixed.put button1, 240, 170
		fixed.put button2, 240, 220
        	fixed.put button3, 685, 180
		fixed.put button4, 600, 180
		fixed.put button5, 240, 300
		fixed.put button6, 240, 370
		
		set_title "Ruby Client"
        	@tes = signal_connect "destroy" do 
			Gtk.main_quit 
			if @tes
				#summary
				showcase
			end	
		end  
		
        	set_default_size 800, 415
        	set_window_position(:center)
        	show_all
	  rescue e
		puts "Sorry, you are not allowed to do this!"
	  end
    end
	
	# Value of User_name entry box
	def user_key_release sen, eve
		@usernme = sen.text
	end
	
	# Value of Pass_word entry box
	def pass_key_release pas, event0
		@passuser = pas.text
	end
	
	def url_key_release sen, eve
		@url = sen.text
	end

	# Value of entry box 1
	def on_key_release sender, event
		@snd = sender.text
    	end
	
	# Value of entry box 2
	def on_key_release1 sender1, event1
		@snd1 = sender1.text
	end
	
	# Value of entry box 3
	def on_key_release2 sender2, event2
		@snd2 = sender2.text
	end
	
	# Value of Download text box
	def on_download_pressed sender3, event3
		@dwnload = sender3.text
	end
	
#***************************************************************************************************************
	def transfer ul, content
        	begin 
			request = Typhoeus::Request.new("http://ignite-now.us", followlocation: true)

			request.on_complete do |response|
				if response.success? or !testing
					puts " hell yeah"
					on_info
				elsif response.code == 0
					puts " Could not get an http response, something's wrong."
					puts "#{response.return_message}"
					on_error
				else
					#    # Received a non-successful http response.
					puts "HTTP request failed: \" + \" #{response.code.to_s}"
					on_error
				end
			end
			request.run
			testing = Typhoeus.post(
				"#{ul}",
			body: {
				userfile: File.open("#{content}","r")
				}
			)
			puts "-----------testing upload------------"
			puts "#{testing}"
		rescue
			on_error
		end	
	end
   
#*************************************************************************************************************	
	def msg link = "."
		if @success or @success_download
			@statement = %{Summary:
		
			Bye...
		
			Current time : #{Time.now}
		
			Activities done in this session are-
		
			Uploaded to : #{link}.
		
			File details:
		
			1) Uploaded file : #{@snd}.
			2) Uploaded file : #{@snd1}.
			3) Uploaded file : #{@snd2}.
			
			Downloaded : #{@dwnload}.
			
			Thank you. Visit again!
			Your files are safe with us!
			}
		end		# Added if else loop.
		if @fail or @fail_download	
			@statement = %{Summary:
		
			Bye...
			
			Current time: #{Time.now}
			
			Sorry! one or more files were not uploaded/downloaded...
			}
		end
	end

   def on_info
        md = Gtk::MessageDialog.new :parent => self, 
            :flags => :destroy_with_parent, :type => :info, 
            :buttons_type => :OK, :message => "Successfully Uploaded"
        @success = md.run
        md.destroy
    end
	puts "^^^^^^^^^^^^^^^^^#{@success}^^^^^^^^^^^^^^^"
	def on_error
       		md = Gtk::MessageDialog.new :parent => self, 
           	:flags => :destroy_with_parent, :type => :info, 
           	:buttons_type => :OK, :message => "Something went Wrong! Failed to upload. Verify again!"
       		@fail = md.run
       		md.destroy
    	end
	puts "^^^^^^^^^^^^^^^^^#{@fail}^^^^^^^^^^^^^^^"

	def showcase
		md = Gtk::MessageDialog.new :parent => self, 
		:flags => :destroy_with_parent, :type => :info, 
		:buttons_type => :OK, :message => "#{@statement}"
		md.run
		md.destroy
    	end
	
	def login uname, pname
		url = "http://ignite-now.us/queryDB.php"
		query_name = "#{uname}"
		query_pass = "#{pname}"
		@result = RestClient.post(url, {'query' => query_name, 'queryp' => query_pass})
		puts "---------------print @result----------------"
		puts @result
		puts query_name
		pattern = /#{query_name}/
		@chk = (@result =~ pattern)
		@chk1 == " "	#added this...
		#if @result =~ pattern
		@cmpre = @chk && !@chk1    #----------------------latest addition
		if @chk && !@chk1
			on_login
		else
			on_error_login
		end
	end
	
	def signup nuser, npass
	
		quering = "http://ignite-now.us/queryDB.php"
		query_name1 = "#{nuser}"
		query_pass1 = "#{npass}"
		@result1 = RestClient.post(quering, {'query' => query_name1, 'queryp' => query_pass1})
		puts "---------------print @result----------------"
		puts @result1
		puts query_name1
		pattern = /#{query_name1}/
		if @result1 =~ pattern
			already_exists
		elsif @chk1
			on_error_login
		else
			request_url = "http://ignite-now.us/backendfile.php"

			@signpage = RestClient.post(request_url, {'firstname' => "#{nuser}", 'lastname' => "#{npass}"})
			puts "------------------------------"
			puts "#{nuser}"
			puts "#{npass}"
			puts "------------------------------"
			puts @signpage
			user_added
			
		end
		
	end
	
	def on_login
		md = Gtk::MessageDialog.new :parent => self, 
        	:flags => :destroy_with_parent, :type => :info, 
        	:buttons_type => :OK, :message => "Welcome!"
        	md.run
        	md.destroy
	end
	
	def on_error_login
		md = Gtk::MessageDialog.new :parent => self, 
        	:flags => :destroy_with_parent, :type => :info, 
        	:buttons_type => :OK, :message => "You are not a valid user. Sign up now!"
        	md.run
        	md.destroy
	end
	
	def user_added
		md = Gtk::MessageDialog.new :parent => self, 
        	:flags => :destroy_with_parent, :type => :info, 
        	:buttons_type => :OK, :message => "Added! Try logging in again..."
        	md.run
        	md.destroy
	end
	
	def already_exists
		md = Gtk::MessageDialog.new :parent => self, 
        	:flags => :destroy_with_parent, :type => :info, 
        	:buttons_type => :OK, :message => "Sorry! User already exists..."
        	md.run
        	md.destroy
	end
		
	def view_files
		@ftps = DoubleBagFTPS.new
		@ftps.passive = true
		@ftps.ssl_context = DoubleBagFTPS.create_ssl_context(:verify_mode => OpenSSL::SSL::VERIFY_NONE)
		@ftps.connect('ftp.ignite-now.us')
		@ftps.login(<Your email/user ID>, <Your Password>)
		@ftps.chdir('/test/')
		puts "-------------------------folder Contents of /test/------------------------------"
		@testing = @ftps.nlst	
		puts @testing
		
		@ftps.chdir('/testserver/')
		puts "------------------------folder Contents of /testserver/-------------------------"
		@testingserver = @ftps.nlst
		puts @testingserver
		
		md = Gtk::MessageDialog.new :parent => self, 
		:flags => :destroy_with_parent, :type => :info, 
		:buttons_type => :OK, :message => "Files stored on the Server 'ignite-now.us' are:
		
			Bye...
		
			Current time : #{Time.now}
			
			Below are the files on Server uploaded by YOU:
				
			#{@testing}
			
			Below are the files on Server uploaded by PARTNER SERVER:
			
			#{@testingserver}
				
			Only the files sent by the Partner Servers can be downloaded.
			Please pass on the name of the file 
			(along with extension .jpg/.txt/.mp3 as such)
			to Download the files."
		md.run
		md.destroy
    	end
		
	def download_server_files(file_name)
		begin
			@ftps = DoubleBagFTPS.new
			@ftps.passive = true
			@ftps.ssl_context = DoubleBagFTPS.create_ssl_context(:verify_mode => OpenSSL::SSL::VERIFY_NONE)
			@ftps.connect('ftp.ignite-now.us')
			@ftps.login('sachinu89@ignite-now.us', 'Wonderstuck8')
			@ftps.chdir('/testserver/')
			@res_file_dwnload = @ftps.get("#{file_name}")
			puts "--------------Download Status----------------"
			#puts @res_file_dwnload
			if !@ftps.get("#{file_name}")
				file_success_download
			else
				error_in_download
			end
		rescue 
			error_in_download
		end
	end
	
	def file_success_download
		md = Gtk::MessageDialog.new :parent => self, 
        	:flags => :destroy_with_parent, :type => :info, 
        	:buttons_type => :OK, :message => "Successfully downloaded the file."
        	@success_download = md.run
        	md.destroy
	end
	
	def error_in_download
		md = Gtk::MessageDialog.new :parent => self, 
        	:flags => :destroy_with_parent, :type => :info, 
        	:buttons_type => :OK, :message => "Sorry! error in file download..."
        	@fail_download = md.run
        	md.destroy
	end
end

Gtk.init
    window = RubyApp.new
Gtk.main
