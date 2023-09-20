// Define a function to handle the form submission
function submitForm(event) {
    // Prevent the default behavior of the form
    event.preventDefault();
    // Get the user input from the input field
    var userInput = $("#user-input").val();
    // Check if the user input is not empty
    if (userInput) {
        // Create a div to display the user's message
        var userMessage = $("<div></div>");
        // Add the alert and alert-primary classes to style the message
        userMessage.addClass("alert alert-primary");
        // Add the user input as the text of the message
        userMessage.text(userInput);
        // Append the message to the chatbot body
        $("#chatbot-body").append(userMessage);
        // Scroll to the bottom of the chatbot body
        $("#chatbot-body").scrollTop($("#chatbot-body")[0].scrollHeight);
        // Clear the input field
        $("#user-input").val("");
        // Disable the input field and the send button
        $("#user-input").prop("disabled", true);
        $("#send-button").prop("disabled", true);
        // Create an object to store the data to be sent to the chatbot endpoint
        var data = {
            "user_input": userInput
        };
        // Use the fetch API to send a POST request to the chatbot endpoint with the data as JSON
        fetch("/chatbot", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        // Convert the response to JSON
        .then(response => response.json())
        // Use the response data to display the chatbot's message and perform the action
        .then(data => {
            // Get the chatbot's message from the data
            var chatbotMessage = data["message"];
            // Get the chatbot's action from the data
            var chatbotAction = data["action"];
            // Create a div to display the chatbot's message
            var botMessage = $("<div></div>");
            // Add the alert and alert-info classes to style the message
            botMessage.addClass("alert alert-info");
            // Add the chatbot's message as the HTML of the message
            botMessage.html(chatbotMessage);
            // Append the message to the chatbot body
            $("#chatbot-body").append(botMessage);
            // Scroll to the bottom of the chatbot body
            $("#chatbot-body").scrollTop($("#chatbot-body")[0].scrollHeight);
            // Enable the input field and the send button
            $("#user-input").prop("disabled", false);
            $("#send-button").prop("disabled", false);
            // Focus on the input field
            $("#user-input").focus();
            // Check if the chatbot's action is not empty
            if (chatbotAction) {
                // Perform the chatbot's action based on its value
                switch (chatbotAction) {
                    case "show_product":
                        // Redirect the user to the product page
                        window.location.href = "/product";
                        break;
                    case "show_demo":
                        // Redirect the user to the demo page
                        window.location.href = "/demo";
                        break;
                    default:
                        // Do nothing
                        break;
                }
            }
        })
        // Catch any error and display it in the console
        .catch(error => console.error(error));
    }
}

// Attach an event listener to the form submission
$("#chatbot-form").submit(submitForm);
