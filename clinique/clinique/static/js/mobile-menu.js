(function(){
  function qs(selector, root){ return (root||document).querySelector(selector); }
  function qsa(selector, root){ return (root||document).querySelectorAll(selector); }

  function openMenu(overlay, button){
    overlay.classList.add('active');
    overlay.setAttribute('aria-hidden','false');
    button.setAttribute('aria-expanded','true');
    // focus first link
    var first = qs('.mobile-menu-card a', overlay);
    if(first) first.focus();
    // prevent body scroll
    document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow = 'hidden';
  }

  function closeMenu(overlay, button){
    overlay.classList.remove('active');
    overlay.setAttribute('aria-hidden','true');
    button.setAttribute('aria-expanded','false');
    document.documentElement.style.overflow = '';
    document.body.style.overflow = '';
    // return focus to button
    button.focus();
  }

  function init(){
    var button = qs('.mobile-menu-button');
    var overlay = qs('#mobile-menu');
    var cancel = qs('.mobile-menu-cancel', overlay);
    if(!button || !overlay || !cancel) return;

    // open
    button.addEventListener('click', function(){ openMenu(overlay, button); });
    // cancel
    cancel.addEventListener('click', function(){ closeMenu(overlay, button); });
    // click outside card closes
    overlay.addEventListener('click', function(e){
      if(e.target === overlay){ closeMenu(overlay, button); }
    });

    // close on ESC
    document.addEventListener('keydown', function(e){
      if(e.key === 'Escape' && overlay.classList.contains('active')){
        closeMenu(overlay, button);
      }
    });

    // trap focus inside modal (basic)
    overlay.addEventListener('keydown', function(e){
      if(e.key !== 'Tab' || !overlay.classList.contains('active')) return;
      var focusable = Array.prototype.slice.call(overlay.querySelectorAll('a, button'));
      if(focusable.length === 0) return;
      var idx = focusable.indexOf(document.activeElement);
      if(e.shiftKey){
        if(idx === 0){ focusable[focusable.length-1].focus(); e.preventDefault(); }
      } else {
        if(idx === focusable.length -1){ focusable[0].focus(); e.preventDefault(); }
      }
    });
  }

  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();