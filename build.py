from pathlib import Path
from html import escape
import re, hashlib, json
ROOT=Path(__file__).resolve().parent
D=ROOT/'dist'
SOURCE=ROOT/'reference'
EMAIL='braxton@bbytechnologies.com'
def E(s):return escape(s,quote=True)
def head(title,description,home=False):
 return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)} | BBY Technologies</title><meta name="description" content="{E(description)}">
<meta name="robots" content="noindex,nofollow"><meta name="color-scheme" content="dark"><meta name="theme-color" content="#202123">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="fonts/playfair-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="tech-hero.css"><link rel="stylesheet" href="bby-header-component.css"><link rel="stylesheet" href="clients.css"><link rel="stylesheet" href="site-dark.css"><link rel="stylesheet" href="complete.css">
<script src="script.js" defer></script></head><body class="home-page {'landing-page' if home else 'inner-page'}">
<a class="skip-link" href="#main-content">Skip to content</a>'''
def header(current=''):
 def link(url,label,cls=''):
  return f'<a href="{url}"'+(f' class="{cls}"' if cls else '')+(' aria-current="page"' if current==url else '')+f'>{label}</a>'
 return '''<header class="site-header"><a class="brand" href="index.html#top" aria-label="BBY Technologies home"><span class="brand-mark">BBY</span><span class="brand-name">Technologies</span></a>
<button class="menu-button" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav id="site-nav" class="site-nav" aria-label="Primary navigation"><div class="nav-dropdown"><button class="nav-dropdown-toggle" type="button" aria-expanded="false" aria-controls="services-menu">Services <span aria-hidden="true">⌄</span></button>
<div id="services-menu" class="nav-dropdown-menu" hidden><div><p class="nav-group-label">Your space</p>'''+''.join(link(*x) for x in [('restaurants.html','Restaurants &amp; Venues'),('small-business.html','SMB'),('residential.html','Residential')])+'''</div><div><p class="nav-group-label">Explore services</p>'''+''.join(link(*x) for x in [('infrastructure.html','Networks &amp; Websites'),('cybersecurity.html','Cybersecurity'),('data.html','Data &amp; Files')])+'''</div></div></div>'''+link('how-it-works.html','How It Works')+link('about.html','About')+link('contact.html','Contact','nav-contact')+'''</nav></header>'''
def footer():
 return '''<footer class="site-footer section-shell"><div class="footer-top"><div><a class="brand" href="index.html"><span class="brand-mark">BBY</span><span class="brand-name">Technologies</span></a><p>Simple technology. Real-world help.</p></div><nav aria-label="Footer navigation"><a href="restaurants.html">Restaurants &amp; Venues</a><a href="small-business.html">SMB</a><a href="residential.html">Residential</a><a href="how-it-works.html">How It Works</a><a href="about.html">About</a><a href="contact.html">Contact</a></nav><div class="footer-contact"><a href="mailto:braxton@bbytechnologies.com">braxton@bbytechnologies.com</a><a href="tel:+17373335763">737-333-5763</a></div></div><div class="footer-bottom"><p>© <span id="year">2026</span> BBY Technologies. Austin, Texas.</p><a href="index.html#top">Back to top ↑</a></div></footer></body></html>'''
def cta(title='Let’s make your technology work better.',desc='Tell me about your space and what you would like to improve.'):
 return f'''<section class="next-step section-shell"><div><p class="eyebrow">A good place to start</p><h2>{E(title)}</h2><p>{E(desc)}</p></div><a class="button button-primary" href="contact.html">Start a Conversation</a></section>'''
def intro(title,desc,eyebrow='Services',art=False):
 return f'''<section class="page-intro section-shell {'with-art' if art else ''}"><div class="intro-copy"><p class="eyebrow">{E(eyebrow)}</p><h1>{E(title)}</h1><p class="page-lead">{E(desc)}</p></div>{'<img class="intro-art" src="tech-hero-spectrum.webp" alt="" width="1600" height="900" decoding="async">' if art else ''}</section>'''
def cards(items):
 return '<div class="detail-grid">'+''.join(f'<article class="detail-card"><span class="detail-index" aria-hidden="true">{i:02}</span><h3>{E(t)}</h3><p>{E(d)}</p></article>' for i,(t,d) in enumerate(items,1))+'</div>'
def links(items):
 return '<div class="service-links">'+''.join(f'<a class="service-row" href="{url}"><div><h3>{E(t)}</h3><p>{E(d)}</p></div><span aria-hidden="true">↗</span></a>' for url,t,d in items)+'</div>'
def page(file,title,desc,body,art=False,eyebrow='Services'):
 (D/file).write_text(head(title,desc)+header(file)+'<main id="main-content" tabindex="-1"><div id="top"></div>'+intro(title,desc,eyebrow,art)+body+'</main>'+footer())
# Keep the exact approved hero; complete the rest of the homepage.
original=(SOURCE/'dist/index.html').read_text()
hero=re.search(r'    <section class="hero section-shell">.*?    </section>',original,re.S).group(0)
hero=hero.replace('href="#contact"','href="contact.html"')
clients=re.search(r'    <div class="clients-backdrop">.*?    </div>\s*\n\s*<section id="services"',original,re.S).group(0).rsplit('<section id="services"',1)[0]
clients=clients.replace('        <p class="eyebrow">Our Favorite Clients</p>\n','')
body='''<section id="services" class="content-section section-shell"><div class="section-heading"><p class="eyebrow">What We Do</p><h2>Technology for your space</h2></div><div class="pillar-grid audience-grid">
<a class="pillar-card audience-card" href="restaurants.html"><h3>Restaurants &amp; Venues</h3></a><a class="pillar-card audience-card" href="small-business.html"><h3>SMB</h3></a><a class="pillar-card audience-card" href="residential.html"><h3>Residential</h3></a></div></section>
<section id="process" class="content-section process-section"><div class="section-shell"><div class="section-heading"><p class="eyebrow">How It Works</p><h2>Advice first. Help when you need it.</h2></div><div class="process-grid">
<article class="process-step"><span>1</span><div><h3>We Talk</h3><p>Tell me what is working, what is not, and what you want to improve.</p></div></article>
<article class="process-step"><span>2</span><div><h3>We Make a Plan</h3><p>Clear recommendations, priorities, and a scope you understand.</p></div></article>
<article class="process-step"><span>3</span><div><h3>I Put It in Place</h3><p>When you are ready, I handle the work and walk you through the result.</p></div></article></div><a class="text-link section-link" href="how-it-works.html">See how it works <span aria-hidden="true">→</span></a></div></section>
<section class="content-section section-shell"><div class="section-heading"><p class="eyebrow">Practical Help</p><h2>Less friction. More useful technology.</h2></div><div class="project-grid">
<a class="project-card linked-card" href="professional-networks.html"><h3>Better Connections</h3><p>Wi-Fi and networks built around your space and devices.</p><span class="card-link">Explore networks <span aria-hidden="true">→</span></span></a>
<a class="project-card linked-card" href="cybersecurity.html"><h3>Stronger Protection</h3><p>Practical ways to protect your accounts, devices, and information.</p><span class="card-link">Explore security <span aria-hidden="true">→</span></span></a>
<a class="project-card linked-card" href="data.html"><h3>Simpler Work</h3><p>Organized files, clear reporting, and less repetitive work.</p><span class="card-link">Explore data <span aria-hidden="true">→</span></span></a></div></section>
<section id="about" class="content-section about-section section-shell"><div class="about-card"><div><p class="eyebrow">About BBY Technologies</p><h2>Local help.<br>Plain language.</h2></div><div><p>Based in Austin, BBY Technologies helps businesses and homes make practical technology improvements—without the sales pressure.</p><a class="text-link" href="about.html">A little about BBY <span aria-hidden="true">→</span></a></div></div></section>
<section id="contact" class="contact-section"><div class="section-shell contact-inner"><p class="eyebrow">Get in touch</p><h2>What would you like to improve?</h2><p>Start with a question. We will take it from there.</p><div class="contact-actions"><a class="button button-light" href="mailto:braxton@bbytechnologies.com">Email Braxton</a><a class="text-link" href="tel:+17373335763">737-333-5763</a></div></div></section>'''
(D/'index.html').write_text(head('Simple technology that works for you','Practical technology help for restaurants, small businesses, and homes. Austin-based networks, security, websites, and data services.',True)+header()+'<main id="main-content" tabindex="-1"><div id="top"></div>'+hero+clients+body+'</main>'+footer())
# Audience pages: simple entry points to the retained services.
audiences={
 'restaurants.html':('Restaurants & Venues','Technology that keeps up with your floor.','For restaurants and venues',[
 ('toast-pos-networks.html','POS & Toast Networks','Keep your payment devices, handhelds, and back office connected.'),
 ('network-optimization.html','Wi-Fi & Connected Devices','Improve coverage for guests, staff, audio, and the devices you depend on.'),
 ('cybersecurity.html','Security That Fits Your Setup','Separate guest access and strengthen the systems behind your business.')],
 '<section class="brand-bridge section-shell"><div><p class="eyebrow">Restaurant-focused support</p><h2>Meet BBY Restaurants.</h2><p>For restaurant networks, POS connectivity, and ongoing technology management, explore BBY Restaurants.</p></div><a class="button button-primary" href="https://bbyrestaurants.com/">Visit BBY Restaurants <span aria-hidden="true">↗</span></a></section>'),
 'small-business.html':('Technology for small business.','Give your team fewer workarounds and a setup that makes sense.','SMB',[
 ('professional-networks.html','Networks & Wi-Fi','Reliable connections for your team, customers, and everyday devices.'),
 ('cybersecurity.html','Accounts & Security','Practical protection for the information your business relies on.'),
 ('data-storage.html','Microsoft 365 & Files','Organize shared files, access, and migrations without the clutter.'),
 ('custom-websites.html','Custom Websites','A clear, useful website that helps people find you and get in touch.'),
 ('data-analysis.html','Reporting & Workflows','Bring scattered information together and simplify repetitive work.')],''),
 'residential.html':('Technology that feels at home.','Better connections for work, streaming, and everyday life.','Residential',[
 ('professional-networks.html','Whole-Home Wi-Fi','Plan coverage around your rooms, devices, and the way you use them.'),
 ('network-optimization.html','Home Office & Connected Devices','Find what is slowing things down and improve your existing setup.'),
 ('cybersecurity-consulting.html','Practical Security','Make sense of account protection, updates, and home-network settings.'),
 ('data-storage.html','Files & Backups','Keep important files organized and plan for recovery when things go wrong.')],'')}
for file,(title,desc,brow,items,extra) in audiences.items():
 page(file,title,desc,'<section class="content-section section-shell audience-services"><div class="section-heading"><p class="eyebrow">How I can help</p><h2>A setup built around you.</h2></div>'+links(items)+'</section>'+extra+cta(),True,brow)
# Existing service categories retained with concise, linked summaries.
categories={
 'infrastructure.html':('Networks & Websites','Build a useful foundation for the way you work.',[
 ('professional-networks.html','Professional Networks','Plan and build connections for your business, home, or home office.'),('network-optimization.html','Network Optimization','Find weak spots and get more from your existing setup.'),('custom-websites.html','Custom Websites','A clear, mobile-friendly home for your business online.'),('toast-pos-networks.html','Toast POS Networks','Restaurant connectivity built around your point-of-sale system.')]),
 'cybersecurity.html':('Practical cybersecurity.','Protect what matters, without making everything harder.',[
 ('cybersecurity-consulting.html','Security Consulting','Understand your current setup and what to improve first.'),('cybersecurity-solutions.html','Security Solutions','Put practical account, network, and device protections in place.')]),
 'data.html':('Make your information useful.','Files that are easier to find. Information that is easier to understand.',[
 ('data-storage.html','Storage & Backups','Organize files, manage access, and plan for recovery.'),('data-analysis.html','Reporting & Workflows','Bring data together and turn it into something you can use.')])}
for file,(title,desc,items) in categories.items():page(file,title,desc,'<section class="content-section section-shell category-section">'+links(items)+'</section>'+cta(),True)
# Complete every retained detailed service route, without technical filler or unsupported promises.
services={
 'professional-networks.html':('Professional networks.','Connections planned around your space, your devices, and your day.','Infrastructure','infrastructure.html','A network that fits.',[
 ('Business Wi-Fi','Separate guest and team access, with coverage where people actually work.'),('Home & Home Office','Support video calls, streaming, smart devices, and everyday use.'),('Wired Connections','Plan cabling and equipment for the devices that need a steady connection.')],['We start with your space, devices, and current internet setup.','Recommendations cover what to keep, what to improve, and what to add.','Installation includes testing and a clear handoff.']),
 'network-optimization.html':('Make your network work better.','Solve connection problems before replacing everything.','Infrastructure','infrastructure.html','Start with the weak spots.',[
 ('Coverage & Speed','Find dead zones, interference, and the bottlenecks behind slow connections.'),('Audio, Cameras & Displays','Check how connected devices are using the network and where they get stuck.'),('Everyday Reliability','Improve placement and settings around how your space is actually used.')],['Describe the problem and when it happens.','We review the network and narrow down the likely causes.','Changes are tested against the problem you came in with.']),
 'custom-websites.html':('A website that works for you.','Clear, useful, and easy for your customers to navigate.','Infrastructure','infrastructure.html','Keep the important things easy.',[
 ('Thoughtful Design','A website that feels like your business, with clear pages and useful content.'),('Mobile-Friendly','Make it easy to browse, call, and get in touch from a phone.'),('A Solid Foundation','Take care of the domain, HTTPS, and the details that keep your site accessible.')],['We agree on your audience, content, and the job your website needs to do.','You review the design and key pages before launch.','The finished site is tested and handed over with clear next steps.']),
 'toast-pos-networks.html':('A network built for Toast.','Connect your POS, handhelds, and back office with a plan for the whole restaurant.','Infrastructure','infrastructure.html','Built around the way you serve.',[
 ('POS & Handheld Connections','Plan wired connections and Wi-Fi coverage around the devices you use.'),('Separate Guest Access','Keep guest traffic separate from the systems running your business.'),('A Clear Network Layout','Make equipment, settings, and connections easier to understand and manage.')],['We review your layout, POS equipment, and existing network.','The plan considers the floor, back office, and other connected systems.','Restaurant-focused details are available through BBY Restaurants.']),
 'cybersecurity-consulting.html':('Know what to protect next.','Straightforward security advice for your accounts, devices, and network.','Cybersecurity','cybersecurity.html','Understand the gaps.',[
 ('Accounts & Access','Review sign-ins, permissions, and how people access important information.'),('Devices & Networks','Look at updates, settings, and the protections already in place.'),('Files & Recovery','Review how important information is backed up and what recovery would involve.')],['We review your existing setup and the things you are concerned about.','Recommendations are prioritized in plain language.','You can act on the advice or get help putting it in place.']),
 'cybersecurity-solutions.html':('Put better protection in place.','Practical security improvements that fit the way you work.','Cybersecurity','cybersecurity.html','Build the missing layers.',[
 ('Accounts & Email','Strengthen sign-ins, access settings, and everyday account protection.'),('Networks & Devices','Configure firewalls, separate access, and improve device protections.'),('Backups & Recovery','Plan backups and check the steps needed to restore important files.')],['We build from your existing tools where they make sense.','Changes are scoped and agreed before implementation.','You get a walkthrough of the changes and what to maintain.']),
 'data-storage.html':('A better home for your files.','Keep information organized, accessible, and easier to recover.','Data','data.html','Find it. Share it. Back it up.',[
 ('Cloud & Shared Files','Organize Microsoft 365, SharePoint, and shared folders around your team.'),('Local Storage','Plan local storage for the files and devices that need it.'),('Migrations & Backups','Move files carefully and put a practical backup and recovery plan in place.')],['We start with where your files are and who needs access.','The plan covers organization, permissions, and how files will move.','We check access and recovery steps with you.']),
 'data-analysis.html':('See what your data is telling you.','Turn spreadsheets and scattered information into something useful.','Data','data.html','Less manual work. More clarity.',[
 ('Dashboards & Reporting','Bring important numbers into a view you can understand and use.'),('Spreadsheet Cleanup','Organize, combine, and check the data you already have.'),('Simple Workflows','Look for practical ways to reduce repeated steps and manual reporting.')],['Start with the question you want your information to answer.','We review the source files and agree on a useful output.','You get a walkthrough of the result and how to keep it current.'])}
for file,(title,desc,category,parent,h2,items,steps) in services.items():
 content='<nav class="breadcrumb section-shell" aria-label="Breadcrumb"><a href="index.html#services">Services</a><span aria-hidden="true">/</span><a href="'+parent+'">'+category+'</a></nav>'
 content+='<section class="content-section section-shell service-details"><div class="section-heading"><p class="eyebrow">What this covers</p><h2>'+E(h2)+'</h2></div>'+cards(items)+'</section>'
 content+='<section class="working-section section-shell"><div><p class="eyebrow">What to expect</p><h2>A clear plan.<br>A practical result.</h2></div><ol class="working-list">'+''.join('<li>'+E(s)+'</li>' for s in steps)+'</ol></section>'
 if file=='toast-pos-networks.html':content+='<div class="section-shell related-link"><a class="text-link" href="https://bbyrestaurants.com/">Explore BBY Restaurants <span aria-hidden="true">↗</span></a><p class="quiet-note">Network design supports your security requirements; it is not a compliance certification.</p></div>'
 content+=cta()
 page(file,title,desc,content,False,category)
# Process, about, and contact are complete pages as well as homepage summaries.
page('how-it-works.html','A simple way to get started.','Advice first. A clear plan. Help putting it in place.','''<section class="content-section section-shell"><div class="steps-expanded"><article><span class="step-number">01</span><div><h2>We Talk</h2><p>Start with your space, the technology you use, and what you want to improve. You do not need to have the technical answers.</p></div></article><article><span class="step-number">02</span><div><h2>We Make a Plan</h2><p>I explain the options and recommend practical next steps. We agree on the scope and cost before work begins.</p></div></article><article><span class="step-number">03</span><div><h2>I Put It in Place</h2><p>When you are ready, I handle the agreed work, check the result, and walk you through what changed.</p></div></article></div></section><section class="faq-section section-shell"><div><p class="eyebrow">Good questions</p><h2>Before we start.</h2></div><div class="faq-list"><details><summary>What should I send you?</summary><p>A short description of your space, the issue or goal, and any timing that matters. Photos or a list of devices can help, but are not needed to start.</p></details><details><summary>Do I need to replace everything?</summary><p>Not necessarily. We start with what you have and look for improvements that make sense before recommending new equipment.</p></details><details><summary>Can I start with advice?</summary><p>Yes. You can start with recommendations and decide how much help you want with implementation.</p></details></div></section>'''+cta(),True,'How It Works')
page('about.html','Local help. Plain language.','Practical technology improvements for businesses and homes.','''<section class="about-story section-shell"><div><p class="eyebrow">BBY Technologies</p><h2>Make technology useful.<br>Keep the process simple.</h2></div><div><p>I’m Braxton. BBY Technologies is my Austin-based technology business.</p><p>I help people make sense of their setup, decide what matters, and put practical improvements in place. That can mean better Wi-Fi, a clearer website, organized files, or stronger account security.</p><p>The goal is straightforward: technology that fits the way you live and work.</p></div></section><section class="content-section section-shell"><div class="section-heading"><p class="eyebrow">The approach</p><h2>Helpful, not complicated.</h2></div>'''+cards([('Start With Your Needs','Understand the problem before choosing a product.'),('Explain the Options','Clear recommendations without unnecessary technical language.'),('Keep It Practical','Build on what works and focus on improvements that matter.')])+'''</section>'''+cta(),True,'About')
page('contact.html','Let’s talk about your technology.','A question, a project, or something that is not working—we can start there.','''<section class="contact-options section-shell"><a class="contact-option" href="mailto:braxton@bbytechnologies.com"><span class="eyebrow">Email Braxton</span><h2>Start a conversation.</h2><p>braxton@bbytechnologies.com</p><span class="contact-arrow" aria-hidden="true">↗</span></a><a class="contact-option phone-option" href="tel:+17373335763"><span class="eyebrow">Call</span><h2>737-333-5763</h2><p>Austin, Texas</p><span class="contact-arrow" aria-hidden="true">↗</span></a></section><section class="contact-note section-shell"><div><h2>A little context helps.</h2><p>Tell me about your space, what you want to improve, and any timing that matters.</p></div><p class="quiet-note">Email opens your mail app. Calling opens your phone app. Nothing is submitted through this website.</p></section><section class="contact-restaurant section-shell"><p>Looking for restaurant-focused services?</p><a class="text-link" href="https://bbyrestaurants.com/">Visit BBY Restaurants <span aria-hidden="true">↗</span></a></section>''',False,'Contact')
page('404.html','That page is not here.','Let’s get you back to the right place.','<section class="section-shell not-found"><a class="button button-primary" href="index.html">Back to Home</a><a class="button button-secondary" href="contact.html">Contact BBY</a></section>',False,'404')
# Static privacy baseline; no tracking, forms, cookies, remote scripts, or runtime dependencies.
(D/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
(D/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#202123"/><path d="M20 14h15c17 0 17 18 5 19 15 2 12 19-4 19H20zm8 7v10h6c8 0 8-10 0-10zm0 17v8h7c8 0 8-8 0-8z" fill="#eff7ff"/></svg>')
# Old page-only PNG illustrations are preserved in the original source, not shipped unused.
for f in D.rglob('*.png'):f.unlink()
if (D/'assets/images').exists(): (D/'assets/images').rmdir()
manifest={'source_project_id':'appgprj_6ae1608b74c08191986eb826f311d1c0','source_checkout':'/workspace/scratch/593dcffee6c5/bbyt-brand-reference','bundled_reference':'reference/dist/index.html','source_commit':'7ae877574205adf674f15b254cce9aaed34960b0','new_project_id':None,'hosting_status':'Local only; native remix capability unavailable. No creation or deployment attempted.','files_preserved_exactly':{f:hashlib.sha256((D/f).read_bytes()).hexdigest() for f in ['styles.css','tech-hero.css','bby-header-component.css','site-dark.css','clients.css','fonts.css','tech-hero-spectrum.webp']}}
(ROOT/'provenance.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Generated',len([f for f in D.glob('*.html') if not f.name.startswith('__')]),'pages')

# Inline stroke icons avoid platform-dependent missing arrow glyphs.
icons = {'↗': '<svg class="arrow-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 19 19 5M5 5h14v14"/></svg>', '→': '<svg class="arrow-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h16m-6-6 6 6-6 6"/></svg>', '↑': '<svg class="arrow-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 20V4m-6 6 6-6 6 6"/></svg>'}
for f in D.glob('*.html'):
 if not f.name.startswith('__qa'):
  text=f.read_text()
  for char,icon in icons.items(): text=text.replace(char,icon)
  f.write_text(text)
