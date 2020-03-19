function setCookie(cname, cvalue, exdays)
{
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname)
{
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function chr4()
{
  return Math.random().toString(16).slice(-4);
}

function get_radio_value(name)
{
  var elements = document.getElementsByName(name);
  var value = "";
  for (var i = 0; i < elements.length; i++)
  {
    if (elements[i].checked)
    {
      value = elements[i].value;
    }
  }
  return value;
}

function get_select_value(id)
{
  var ele = document.getElementById(id)
  return ele.options[ele.selectedIndex].value;
}

function get_input_value(id)
{
  return document.getElementById(id).value
}

function check_data_missing(id)
{
  var eles = document.getElementsByName(id);
  for (i=0; i<eles.length; i++)
  {
    if (eles[i].type == "text")
      return set_missing_id(id, get_input_value(id));
    if (eles[i].type == "select-one")
      return set_missing_id(id, get_select_value(id));
    if (eles[i].type == "radio")
      return set_missing_id(id, get_radio_value(id));
  }
}

function set_missing_name(name, val)
{
  var eles = document.getElementsByName(name)
  for (i=0; i<eles.length; i++)
  {
    if (val == "")
      eles[i].classList.add("has-background-danger");
    else
      eles[i].classList.remove("has-background-danger");
  }
  if (val == "")
    return 1;
  else
    return 0;
}

function set_missing_id(id, val)
{
  var e;
  try {
    e = document.getElementById("label_" + id); 
    if (val == "")
    {
      document.getElementById("label_" + id).classList.add("has-text-danger");
      return 1;
    }
    else
    {
      document.getElementById("label_" + id).classList.remove("has-text-danger");
      return 0;
    }
  } catch {
    alert("set_missing_id could not find label_" + id);
    return 1;
  }
}
