import requests
import bs4
from multiprocessing import Pool


def get_url(url):
    return requests.get(url)


# response = get_url('http://pyvideo.org/events/pycon-jamaica-2016.html')
response = get_url('http://pyvideo.org/events/pycon-ca-2016.html')


def scrapping(response_value, link_type, tag, search_text):
    soup = bs4.BeautifulSoup(response_value, "html.parser")
    return {links.get(link_type) for links in soup.find_all(tag) if search_text in links.get(link_type)}


pycon_youtube_links = scrapping(response.text, 'href', 'a', 'pycon-ca-2016/')


def youtube_page(youtube_link):
    l = []
    for link in youtube_link:
        r = get_url(link)
        l.append(scrapping(r.text, 'src', 'iframe', 'youtube'))
    return l


youtube = youtube_page(pycon_youtube_links)

''' Prints list of Youtube video links '''
''' Example: [{'https://www.youtube.com/embed/7ProkEKjtL4'}, {'https://www.youtube.com/embed/dEMN67J5-NA'}]'''
# print(youtube)


def video_keys(page):
    return [list(item)[0].split('/')[-1] for item in page]


''' Get a list of all the video Keys '''
keys = video_keys(youtube)

''' Prints list of youtube video IDs '''
''' Example: [\'7ProkEKjtL4\', \'dEMN67J5-NA\'] '''
# print(keys)


def visit_youtube_with(key):
    video_data = {}
    status = get_url('https://www.youtube.com/watch?v=' + key)
    soup = bs4.BeautifulSoup(status.text, "html.parser")
    video_data[status.url] = [soup.select('div#watch-headline-title h1 span.watch-title')[0].get_text().strip(),
                              soup.select('.watch-view-count')[0].get_text()]

    return video_data

final_stats = []
with Pool(5) as p:
    final_stats += p.map(visit_youtube_with, keys)

print("Total # of videos: ", str(len(final_stats)))

for record in final_stats:
    print(record)



Sample Output:

Total # of videos:  56
{'https://www.youtube.com/watch?v=dWNxplKYu4M': ['Deep learning techniques for predictive analytics using Python: Theano vs TensorFlow (Allaa Hilal)', '276 views']}
{'https://www.youtube.com/watch?v=JzAjjo_E6iY': ['Managing large ensembles and batch execution with Python (Andre R. Erler)', '64 views']}
{'https://www.youtube.com/watch?v=UKxIswJSlIY': ['Welcome & Morning Keynote (Tracy Osborn)', '297 views']}
{'https://www.youtube.com/watch?v=maploUbsLn4': ["Securing Your company's data: encryption, deletion and other best practices (Elissa Shevinsky)", '155 views']}
{'https://www.youtube.com/watch?v=AAY6TvD9FH4': ['How to write maintainable code without tests (Juti Noppornpitak)', '340 views']}
{'https://www.youtube.com/watch?v=xLc5xPYGGnQ': ['CPython internals: why bother? (James Powell)', '349 views']}
{'https://www.youtube.com/watch?v=emOXFEeL3ec': ['Python and the Blockchain (Anthony Barker)', '672 views']}
{'https://www.youtube.com/watch?v=cVwDGEhk6ck': ['Jupyter Notebooks in the cloud (Brett Cannon)', '184 views']}
{'https://www.youtube.com/watch?v=5NRiW4FF8-0': ['Morning keynote (Safia Abdalla)', '188 views']}
{'https://www.youtube.com/watch?v=tupD_KbjVwI': ['Circuit simulator for power electronics: Python power electronics (Shivkumar V. Iyer)', '106 views']}
{'https://www.youtube.com/watch?v=OBS3FG_MyIg': ["Overcoming life's hurdles (Sarah Wells)", '112 views']}
{'https://www.youtube.com/watch?v=Vx-owGdnEGU': ['G.Tool: a Python-based DSL for managing information security governance information (Ben Sapiro)', '77 views']}
{'https://www.youtube.com/watch?v=SQcCmCyuVyo': ['Hypothesis: tests that write themselves (David Kua)', '192 views']}
{'https://www.youtube.com/watch?v=SRy6P0_FA7I': ['Not on the shelves (Greg Wilson)', '95 views']}
{'https://www.youtube.com/watch?v=ZkAc6hzGun4': ['Architecture of CPython, the bricks! (Stéphane Wirtel)', '160 views']}
{'https://www.youtube.com/watch?v=uvE8FGg5dgY': ['Embrace the mistake (Mike C. Fletcher)', '115 views']}
{'https://www.youtube.com/watch?v=72nuPi43mO4': ['PyCon Canada 2016 Lightning Talks', '296 views']}
{'https://www.youtube.com/watch?v=-ylbuEzkG4M': ['Extending Python with Rust (Samuel Cormier-Iijima)', '3,301 views']}
{'https://www.youtube.com/watch?v=0neAl4mylrE': ['Python to Iron Python to SQL Server (Matt McGraw)', '92 views']}
{'https://www.youtube.com/watch?v=kWNfbiwk0PA': ['Building a HackASac (Paul Mullins)', '165 views']}
{'https://www.youtube.com/watch?v=84BRQgOPYxM': ["Where we came from, what's special about now, and where we might go (Stephen J Turnbull)", '128 views']}
{'https://www.youtube.com/watch?v=dEMN67J5-NA': ['Word! Automating a Hip-hop word of the day blog (Christopher Ing)', '72 views']}
{'https://www.youtube.com/watch?v=JQLfGiK15Oo': ['An end to boring data with visualizations (Heather Shapiro)', '468 views']}
{'https://www.youtube.com/watch?v=O33YV4ooHSo': ['Make some noise with Python and generate terrain (Michael McHugh)', '172 views']}
{'https://www.youtube.com/watch?v=hM9qbW8-roE': ['The art of writing wargames in Python with Kivy (Dorian Pula)', '861 views']}
{'https://www.youtube.com/watch?v=3GNnVSTtl-o': ['"Fabric"ating RESTful APIs for Linux (Sachin Agarwal)', '117 views']}
{'https://www.youtube.com/watch?v=K_b1RBWp8YA': ["When the abyss gazes back: staring down Python's surprising internals (David Wolever)", '415 views']}
{'https://www.youtube.com/watch?v=m_vepmNprDc': ['Mutants and immutants: the missing types (Sye van der Veen)', '138 views']}
{'https://www.youtube.com/watch?v=GMWwiOXHEMg': ['Painful serverless (Hadrien David)', '184 views']}
{'https://www.youtube.com/watch?v=ovvU41ve1FQ': ['Automate your data analysis testing (Stephen Childs)', '107 views']}
{'https://www.youtube.com/watch?v=hk85RUtQsBI': ["What's new in Python 3.6 (Brett Cannon)", '5,653 views']}
{'https://www.youtube.com/watch?v=DefBuK4jXuM': ['State of the PyVideo (Paul Logston)', '139 views']}
{'https://www.youtube.com/watch?v=9Vz7oFjwXOA': ['Creating a contemporary lending risk management system using Python (Piero Ferrante)', '190 views']}
{'https://www.youtube.com/watch?v=-TdrFjDJn5E': ['Afternoon keynote (Raymond Hettinger)', '2,482 views']}
{'https://www.youtube.com/watch?v=DEat8aOk0rA': ['Building and managing diverse engineering teams (Elissa Shevinsky)', '85 views']}
{'https://www.youtube.com/watch?v=z1aUuqKg_gA': ['Using Python to power Selenium at scale (Brandon Rhodes)', '322 views']}
{'https://www.youtube.com/watch?v=U3nNiFGTcKY': ["Hacker's guide to Neural Networks (Anoop Thomas Mathew)", '165 views']}
{'https://www.youtube.com/watch?v=_kES4dCyrvU': ['A concrete approach to abstractions (Terry Yanchynskyy)', '188 views']}
{'https://www.youtube.com/watch?v=yvvUaeovTBU': ['Hockey Night at PyCon (Joshua Weissbock)', '52 views']}
{'https://www.youtube.com/watch?v=Dv1bpmYV0vU': ["Async tasks with Django Channels (Albert O'Connor)", '336 views']}
{'https://www.youtube.com/watch?v=lgLrFPIg1VM': ['Simple made easy (Steve Jackson)', '1,370 views']}
{'https://www.youtube.com/watch?v=6uqEL9vWx1Q': ["Rub-a-dub rubber duck: don't be afraid to debug! (Anna Ossowski)", '91 views']}
{'https://www.youtube.com/watch?v=6WY4xtA5PcA': ['Living in a land down dunder (Paul Logston)', '252 views']}
{'https://www.youtube.com/watch?v=7ProkEKjtL4': ['Version control worst practices (Greg Ward)', '975 views']}
{'https://www.youtube.com/watch?v=_LEff9I1Fnc': ['What kind of sorcery is OpenStack? (Daniel Snider)', '275 views']}
{'https://www.youtube.com/watch?v=hHOvXPhgZoY': ['Quantifying the visual structure of written language (Nick Anderegg)', '97 views']}
{'https://www.youtube.com/watch?v=WSq0S7UvI8E': ['High performance networking in Python (Yury Selivanov)', '403 views']}
{'https://www.youtube.com/watch?v=5i5omk3tYxc': ['Pragmatic microservices for the rest of us (Ryan Easterbrook)', '315 views']}
{'https://www.youtube.com/watch?v=v8ryA-s5eZM': ['Databases 201: the power of the relational algebra and limits of the ORM (Wesley George)', '416 views']}
{'https://www.youtube.com/watch?v=eYTfgbr7b0U': ['How to make ** less expensive and more expressive (en zyme)', '146 views']}
{'https://www.youtube.com/watch?v=gJ4duC-V6Xw': ['Monty Python for pythonistas (sa friend)', '2,047 views']}
{'https://www.youtube.com/watch?v=JM-ce-cS0_E': ['From idea to production in 20 minutes: engineering at scale (Jean-Philippe Caissy)', '200 views']}
{'https://www.youtube.com/watch?v=SMAh9gEIkPo': ['Hacking Cars with Python (Eric Evenchick)', '163 views']}
{'https://www.youtube.com/watch?v=ZGU_fIOMpgk': ['Building the Real-time Web with Python and aiohttp (Steven Seguin)', '519 views']}
{'https://www.youtube.com/watch?v=lI3ipk6j3-k': ["GitHub's Deployments API: let GitHub be your deployment glue (Jay Parlar)", '157 views']}
{'https://www.youtube.com/watch?v=t4yLeP6kFnk': ['See Python, See Python Go, Go Python Go (Andrey Petrov)', '257 views']}
