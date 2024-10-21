# Tests

## Lighthouse

Lighthouse is an open-source tool for improving the quality of web pages. It provides insights into performance, accessibility, best practices, and SEO. Below are the results from Lighthouse tests for various pages and devices.

### Home Page

<details><summary>Desktop</summary>
    <img src="./docs/tests/lighthouse-desktop-home.png" alt="Home Page Desktop">
</details>

<details><summary>Mobile</summary>
    <img src="./docs/tests/lighthouse-mobile-home.png" alt="Home Page Mobile">
</details>

### Shopping Bag Page

<details><summary>Desktop</summary>
    <img src="./docs/tests/lighthouse-desktop-bag.png" alt="Shopping Bag Desktop">
</details>

<details><summary>Mobile</summary>
    <img src="./docs/tests/lighthouse-mobile-bag.png" alt="Shopping Bag Mobile">
</details>

### Contact Page

<details><summary>Desktop</summary>
    <img src="./docs/tests/lighthouse-desktop-contact.png" alt="Contact Page Desktop">
</details>

<details><summary>Mobile</summary>
    <img src="./docs/tests/lighthouse-mobile-contact.png" alt="Contact Page Mobile">
</details>

### FAQs Page

<details><summary>Desktop</summary>
    <img src="./docs/tests/lighthouse-desktop-faqs.png" alt="FAQs Page Desktop">
</details>

<details><summary>Mobile</summary>
    <img src="./docs/tests/lighthouse-mobile-faqs.png" alt="FAQs Page Mobile">
</details>

### Products Listing Page

<details><summary>Desktop</summary>
    <img src="./docs/tests/lighthouse-desktop-products.png" alt="Products Listing Desktop">
</details>

<details><summary>Mobile</summary>
    <img src="./docs/tests/lighthouse-mobile-products.png" alt="Products Listing Mobile">
</details>

### Individual Product Page

<details><summary>Desktop</summary>
    <img src="./docs/tests/lighthouse-desktop-view-product.png" alt="Individual Product Page Desktop">
</details>

<details><summary>Mobile</summary>
    <img src="./docs/tests/lighthouse-mobile-view-product.png" alt="Individual Product Page Mobile">
</details>

## Code Validation

### HTML

### HTML Validation

The HTML validation process was conducted using the [Nu HTML Checker](https://validator.w3.org/). Below are the results for various pages on the website, highlighting any errors and warnings found.

<details><summary>Checkout Page Validation</summary>
    <img src="./docs/tests/checkout-html-validation.png" alt="HTML Validation - Checkout Page">
</details>

<details><summary>Home Page Validation</summary>
    <img src="./docs/tests/home-html-validation.png" alt="HTML Validation - Home Page">
</details>

<details><summary>Login Page Validation</summary>
    <img src="./docs/tests/login-html-validation.png" alt="HTML Validation - Login Page">
</details>

<details><summary>Register Page Validation</summary>
    <img src="./docs/tests/register-html-validation.png" alt="HTML Validation - Register Page">
</details>

<details><summary>Shopping Bag Page Validation</summary>
    <img src="./docs/tests/bag-html-validation.png" alt="HTML Validation - Shopping Bag Page">
</details>

### Explanation of Errors

1. **Invalid `li` Elements Inside `nav` and Duplicate IDs**:  
   Several instances where `<li>` elements were placed directly inside `<nav>` elements instead of being wrapped in an unordered list (`<ul>`). This is because I folowed the Boutiq Ado walktru and keep 2 menus, one for desktop and one for mobile, both had the same ID.

### CSS

<details><summary>base.css</summary>
    <img src="./docs/tests/base-css-test.png" alt="base.css test results">
</details>

<details><summary>checkout.css</summary>
    <img src="./docs/tests/checkout-css-test.png" alt="base.css test results">
</details>

### Python

### PEP8 Validation

PEP8 validation was performed on all Python files in the project to ensure adherence to Python's style guide. Below are the results and highlights of each file:

<details><summary>Products Models</summary>
    <img src="./docs/tests/pep8-products-models.png" alt="PEP8 Products Models">
</details>

<details><summary>Products Views</summary>
    <img src="./docs/tests/pep8-products-views.png" alt="PEP8 Products Views">
</details>

<details><summary>Profiles Models</summary>
    <img src="./docs/tests/pep8-profiles-models.png" alt="PEP8 Profiles Models">
</details>

<details><summary>Profiles Views</summary>
    <img src="./docs/tests/pep8-profiles-views.png" alt="PEP8 Profiles Views">
</details>

<details><summary>Reviews Models</summary>
    <img src="./docs/tests/pep8-reviews-model.png" alt="PEP8 Reviews Models">
</details>

<details><summary>Reviews Views</summary>
    <img src="./docs/tests/pep8-reviews-views.png" alt="PEP8 Reviews Views">
</details>

<details><summary>Wishlist Models</summary>
    <img src="./docs/tests/pep8-wishlist-model.png" alt="PEP8 Wishlist Models">
</details>

<details><summary>Wishlist Views</summary>
    <img src="./docs/tests/pep8-wishlist-views.png" alt="PEP8 Wishlist Views">

</details>

Each issue identified primarily revolves around line length (E501). These issues can be resolved by breaking long lines into shorter ones or restructuring the code for clarity.

## Browser Testing

The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.

## Device Testing

The website was tested on a variety of devices, including Desktop, and Samsung S21, to ensure that it displayed well on screens of different sizes, both in portrait and landscape orientations. The website functioned as expected, and its responsive design was validated using Chrome developer tools on various devices, ensuring that the layout remained structurally sound across different screen dimensions.

## Manual Testing

### Homepage

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Verify Homepage Load                  | 1. Open the homepage URL.<br>2. Check page content.     | Homepage loads correctly with all sections displayed. | PASS    |
| Check Navigation Links                | 1. Click on each navigation link.<br>2. Verify redirection to corresponding pages. | Links redirect to the correct pages.       | PASS    |
| Test Responsive Design                | 1. Resize the browser window to various screen sizes.<br>2. Verify layout adapts appropriately. | Layout adjusts correctly for mobile, tablet, and desktop views. | PASS    |
| Verify Call-to-Action Buttons         | 1. Click each CTA button.<br>2. Ensure button redirects or performs the intended action. | Buttons perform actions as expected (e.g., redirect, open form). | PASS    |
| Test Search Functionality             | 1. Enter keywords in the search bar.<br>2. Press enter and verify results. | Results matching the search term are displayed correctly. | PASS    |

### Product Page

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Verify Product Details Display        | 1. Navigate to a product page.<br>2. Check product information (image, price, description). | Product details are displayed accurately. | PASS    |
| Test Add to Bag Functionality        | 1. Click on "Add to Bag" button.<br>2. Check the Bag icon for update. | Product is added to the Bag successfully, and the Bag count increases. | PASS    |
| Validate Quantity Selection           | 1. Adjust product quantity using the selector.<br>2. Click "Add to Bag" and verify Bag reflects correct quantity. | Bag updates to reflect the selected quantity accurately. | PASS    |
| Test Responsive Design                | 1. Resize the browser window to mobile/tablet sizes.<br>2. Ensure product layout adjusts appropriately. | Product layout is responsive and displays correctly on different screen sizes. | PASS    |

### Bag Page

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Verify Bag Page Load                 | 1. Navigate to the Bag page.<br>2. Check for product list and total price. | Bag displays all added products with correct details. | PASS    |
| Test Quantity Update                  | 1. Change the quantity of a product in the Bag.<br>2. Verify total price updates. | Bag updates correctly when quantity is changed. | PASS    |
| Remove Product from Bag              | 1. Click "Remove" on a product.<br>2. Check if product is removed from the Bag and total price adjusts. | Product is removed and Bag updates accurately. | PASS    |
| Test Checkout Button                  | 1. Click the "Proceed to Checkout" button.<br>2. Ensure user is redirected to the checkout page. | Checkout page opens after clicking the button. | PASS    |

### Checkout Page

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Verify Form Validation                | 1. Leave fields empty and attempt to submit.<br>2. Observe validation messages. | Appropriate validation messages are displayed for empty fields. | PASS    |
| Test Payment Integration              | 1. Enter valid payment details.<br>2. Submit the form.   | Payment is processed and confirmation message is shown. | PASS    |
| Test Error Handling for Invalid Card  | 1. Enter invalid card details.<br>2. Attempt to submit.  | Error message is displayed, and payment is not processed. | PASS    |

### User Account

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Test Registration Functionality       | 1. Navigate to the "Register" page.<br>2. Fill out form and submit. | User is registered successfully and redirected to the homepage or account page. | PASS    |
| Validate Login Process                | 1. Navigate to the "Login" page.<br>2. Enter credentials and submit. | User is logged in and redirected to their account page. | PASS    |
| Test Password Reset                   | 1. Click on "Forgot Password" link.<br>2. Enter email and follow instructions. | Password reset email is sent successfully. | PASS    |

### Wishlist Functionality

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Add Product to Wishlist               | 1. Navigate to a product page.<br>2. Click "Add to Wishlist". | Product is added to the wishlist and confirmation is shown. | PASS    |
| Verify Wishlist Display               | 1. Navigate to the "Wishlist" page.<br>2. Check for added products. | Products added to the wishlist are displayed correctly. | PASS    |
| Remove Product from Wishlist          | 1. Click "Remove" on a product in the wishlist.<br>2. Confirm product is removed. | Product is removed from the wishlist successfully. | PASS    |

### Footer and Links

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Verify Footer Display                 | 1. Scroll to the bottom of any page.<br>2. Ensure footer content is visible and correct. | Footer displays correctly with all links and information. | PASS    |
| Test Footer Links                     | 1. Click each footer link.<br>2. Ensure it redirects to the correct page. | Footer links work and direct to the appropriate pages. | PASS    |
| Test Newsletter                       | 1. Enter email address<br>2. Ensure mailchimp sents a confirmation message. | Confirmation message successfully. | PASS    |

### Contact Page

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Verify Contact Form Display           | 1. Navigate to the contact page.<br>2. Ensure all form fields are visible. | Contact form displays correctly with all fields. | PASS    |
| Test Form Submission                  | 1. Fill out the contact form with valid information.<br>2. Click "Submit". | Form submits successfully, and a confirmation message is shown. | PASS    |
| Validate Form Error Handling          | 1. Leave fields empty or enter invalid information.<br>2. Attempt to submit the form. | Error messages display correctly, preventing form submission. | PASS    |

### FAQs Page

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Verify FAQs Load                      | 1. Open the FAQs page URL.<br>2. Ensure all questions and answers are displayed. | FAQs are loaded and displayed correctly. | PASS    |
| Test Collapsible Functionality        | 1. Click on a question.<br>2. Verify if the answer expands/collapses as expected. | Clicking on a question expands and collapses the answer section correctly. | PASS    |
| Test Responsive Design                | 1. Resize the browser window to various screen sizes.<br>2. Ensure FAQs layout adjusts accordingly. | FAQs display correctly across all screen sizes. | PASS    |

### Reviews Section

| Test Case                             | Steps                                                    | Expected Result                             | Status |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------|--------|
| Verify Reviews Display                | 1. Navigate to a product page with reviews.<br>2. Scroll to the reviews section. | Reviews are displayed correctly with user details and ratings. | PASS    |
| Test Adding a Review                  | 1. Navigate to a product page.<br>2. Click "Add Review".<br>3. Submit a review. | Review is submitted and appears in the list. | PASS    |
| Validate Review Submission Error Handling | 1. Attempt to submit a review without logging in.<br>2. Observe the error message. | User is prompted to log in before submitting a review. | PASS    |


