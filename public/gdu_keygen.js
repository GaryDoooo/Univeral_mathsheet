// it's to generate a random client key toString

function client_random_key_gen() {
  var result = date_time_string();
  console.log(result,"from date_time_string");
  return Math.floor(Math.random() * 1000000).toString(36) + "GD" + //result.toString(36);
    Number(result).toString(36);
}

//////// Generate current datetime string
var date_time_string = function() {
  var usaTime = new Date().toLocaleString("en-US", {
    timeZone: "America/New_York"
  });
  var currentdate = new Date(usaTime);
  var month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
  ];
  return currentdate.getDate() + "0"+
    currentdate.getHours() +
    currentdate.getMinutes() +
    currentdate.getSeconds();
};
