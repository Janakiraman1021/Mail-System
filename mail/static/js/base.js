        // Get the list of email links
        const emailLinks = document.querySelectorAll('.email-link');

        // Add a click event listener to each email link
        emailLinks.forEach(emailLink => {
          emailLink.addEventListener('click', event => {
            // Prevent the default link behavior
            event.preventDefault();
        
            // Get the href of the clicked email link
            const href = emailLink.getAttribute('href');
        
            // Use fetch to get the email content from the server
            fetch(href)
              .then(response => response.text())
              .then(emailContent => {
                // Create a new div to display the email content
                const emailDiv = document.createElement('div');
                emailDiv.innerHTML = emailContent;
        
                // Replace the email link with the email content
                emailLink.parentNode.replaceChild(emailDiv, emailLink);
              })
              .catch(error => {
                console.error(error);
              });
          });
        });