var myform = $("form#contactForm");
myform.submit(function(event){
    event.preventDefault();

  // Change to your service ID, or keep using the default service
  var service_id = "gmail";
  var template_id = "miscsoletrader";

  $('.btn').prop('disabled', true); // Button Disable
  myform.find("button").text("Wait..."); // Change Button Text
  emailjs.sendForm(service_id,template_id,myform[0])
    .then(function(){ 
       myform.find("button").text("Send"); // Display Sens text on Button
       $('.btn').prop('disabled', false); // Enable Button
       $('#success').show(); // Shhoe success alert
       myform.trigger("reset"); // rest all fileds on form
    }, function(err) {
       myform.find("button").text("Send");
    });
  return false;
});







/*    alert("hi");
    emailjs.sendForm('gmail', 'template_EUYyvjOQ', this);
}*/

//console.log('Hello');

/*emailjs.send("gmail", "miscsoletrader", {
    "from_name":"H Mansuri",
    "from_email":"hidayat.mansuri@gmail.com",
    "from_amazon":"132-54654-654564",
    "website_contact":"Hi,"
    
})var templateParams = {
    name: 'James',
    notes: 'Check this out!'
};

var templateParams = {
    name: 'James',
    notes: 'Check this out!'
};
 
emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams)
    .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
       console.log('FAILED...', error);
    });
*/