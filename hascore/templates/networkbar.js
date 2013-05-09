{% from "baseframe/components.html" import networkbar -%}

(function(){

  var ss1 = document.createElement("link");
  ss1.type = "text/css";
  ss1.rel = "stylesheet";
  ss1.href = "{{ url_for('baseframe.static', filename='css/networkbar.css', _external=True) }}";
  document.getElementsByTagName("head")[0].appendChild(ss1);

  var ss2 = document.createElement("link");
  ss2.type = "text/css";
  ss2.rel = "stylesheet";
  ss2.href = "//fonts.googleapis.com/css?family=Open+Sans:400italic,600italic,400,600;"
  document.getElementsByTagName("head")[0].appendChild(ss2);
  
  var container = document.getElementById('networkbar');
  if (container === null) {
    container = document.createElement('div');
    document.body.insertBefore(container, document.body.firstChild);
  }
  container.innerHTML = {{ networkbar(login=false)|tojson|safe }};
})();
