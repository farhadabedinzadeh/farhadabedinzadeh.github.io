"""Make a self-contained HTML review copy of the built site (beautifulsoup4)."""
from pathlib import Path
import base64,mimetypes
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'_site'
soup=BeautifulSoup((SITE/'index.html').read_text(),'html.parser')
for t in list(soup.select('link,meta[property^="og:"],script')):t.decompose()
soup.title.string='Website preview · Farhad Abedinzadeh'
robots=soup.new_tag('meta');robots['name']='robots';robots['content']='noindex,nofollow';soup.head.append(robots)
css=soup.new_tag('style');css.string=(ROOT/'assets/css/academic.css').read_text()+'\n.preview-panel[hidden]{display:none!important}';soup.head.append(css)
main=soup.select_one('main');home=soup.new_tag('div',id='preview-home');home['class']='preview-panel'
for item in list(main.contents):home.append(item.extract())
main.append(home)
for name in ['publications','cv']:
 page=BeautifulSoup((SITE/name/'index.html').read_text(),'html.parser')
 panel=soup.new_tag('div',id='preview-'+name);panel['class']='preview-panel';panel['hidden']=''
 for item in list(page.main.contents):panel.append(item.extract())
 main.append(panel)
for img in soup.select('img'):
 p=SITE/img['src'].lstrip('/')
 img['src']='data:'+mimetypes.guess_type(p)[0]+';base64,'+base64.b64encode(p.read_bytes()).decode()
for a in soup.select('a[href]'):
 href=a['href']
 if href=='/':a['href']='#about'
 elif href.startswith('/#'):a['href']=href[1:]
 elif href=='/publications/':a['href']='#view-publications'
 elif href=='/cv/':a['href']='#view-cv'
 elif href.startswith('/files/cv/'):
  a['href']='data:application/pdf;base64,'+base64.b64encode((ROOT/href.lstrip('/')).read_bytes()).decode()
  a['download']='Farhad-Abedinzadeh-CV.pdf'
js=soup.new_tag('script');js.string=(ROOT/'assets/js/academic.js').read_text()+'''
(() => {
  const panels = [...document.querySelectorAll('.preview-panel')];
  let active = 'home';
  function route() {
    const hash = decodeURIComponent(location.hash.slice(1));
    if (hash !== 'main') active = hash === 'view-publications' ? 'publications' : hash === 'view-cv' ? 'cv' : 'home';
    panels.forEach(panel => panel.hidden = panel.id !== 'preview-' + active);
    document.querySelectorAll('[aria-current]').forEach(link => link.removeAttribute('aria-current'));
    const current = document.querySelector(active === 'publications' ? 'nav a[href="#view-publications"]' : active === 'cv' ? '.header-cv' : 'nav a[href="#about"]');
    if (current) current.setAttribute('aria-current','page');
    document.title = (active === 'home' ? 'Website preview' : active === 'cv' ? 'Academic CV' : 'Publications') + ' · Farhad Abedinzadeh';
    if (active !== 'home' || !hash || hash === 'main') window.scrollTo(0,0);
    else document.getElementById(hash)?.scrollIntoView();
  }
  addEventListener('hashchange', route);
  route();
})();
''';soup.body.append(js)
out=ROOT/'preview/site-preview.html';out.parent.mkdir(exist_ok=True);out.write_text(str(soup))
print(out,out.stat().st_size,'bytes')
