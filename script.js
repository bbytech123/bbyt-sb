'use strict';
const menuButton = document.querySelector('.menu-button');
const siteNav = document.querySelector('.site-nav');
const dropdown = document.querySelector('.nav-dropdown');
const serviceToggle = document.querySelector('.nav-dropdown-toggle');
const serviceMenu = document.querySelector('#services-menu');
const mobile = window.matchMedia('(max-width: 860px)');
function setServices(open) {
  dropdown?.classList.toggle('open', open);
  serviceToggle?.setAttribute('aria-expanded', String(open));
  if (serviceMenu) serviceMenu.hidden = !open;
}
function setMenu(open) {
  siteNav?.classList.toggle('open', open);
  menuButton?.setAttribute('aria-expanded', String(open));
  if (!open) setServices(false);
}
menuButton?.addEventListener('click', () => setMenu(menuButton.getAttribute('aria-expanded') !== 'true'));
serviceToggle?.addEventListener('click', () => setServices(serviceToggle.getAttribute('aria-expanded') !== 'true'));
document.addEventListener('click', (event) => {
  if (!dropdown?.contains(event.target)) setServices(false);
  if (mobile.matches && !siteNav?.contains(event.target) && !menuButton?.contains(event.target)) setMenu(false);
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  if (serviceToggle?.getAttribute('aria-expanded') === 'true') {
    setServices(false); serviceToggle.focus();
  } else if (menuButton?.getAttribute('aria-expanded') === 'true') {
    setMenu(false); menuButton.focus();
  }
});
siteNav?.addEventListener('focusout', (event) => {
  if (!siteNav.contains(event.relatedTarget) && event.relatedTarget !== menuButton) {
    setServices(false); if (mobile.matches) setMenu(false);
  }
});
siteNav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
mobile.addEventListener('change', () => setMenu(false));
document.querySelectorAll('#year').forEach(el => { el.textContent = String(new Date().getFullYear()); });
