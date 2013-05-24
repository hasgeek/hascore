{% from "baseframe/components.html" import networkbar with context -%}

(function(){
  var head = document.getElementsByTagName('head')[0],
      css = '#hg-bar { display: none; }',
      style = document.createElement('style'),
      sl1 = document.createElement("link"),
      sl2 = document.createElement("link");

  style.type = 'text/css';

  if (style.styleSheet) {
    style.styleSheet.cssText = css;
  } else {
    style.appendChild(document.createTextNode(css));
  }
  head.appendChild(style);

  sl1.type = "text/css";
  sl1.rel = "stylesheet";
  sl1.href = "//fonts.googleapis.com/css?family=Open+Sans:400italic,600italic,400,600";
  head.appendChild(sl1);

  sl2.type = "text/css";
  sl2.rel = "stylesheet";
  sl2.href = "{{ request.url_root[:-1] }}{% assets 'css_networkbar' %}{{ ASSET_URL }}{% endassets %}";
  head.appendChild(sl2);

  var container = document.getElementById('networkbar');
  if (container === null) {
    container = document.createElement('div');
    document.body.insertBefore(container, document.body.firstChild);
  }
  container.innerHTML = {{ networkbar(login=false)|tojson|safe }};

  var siteid = container.getAttribute('data-siteid');
  if (siteid) {
    var menuelement = document.querySelector('#hg-bar [data-siteid="' + siteid + '"]');
    if (menuelement !== null) {
      menuelement.className = menuelement.className + " selected";
    }
  }
})();
