# AI Job Description Generator

This Streamlit application uses Google's Gemini API to generate job descriptions, both formal and funky, based on user input.

## Features

-   **Formal Job Description Generation:** Creates professional and detailed job descriptions.
-   **Funky Job Description Generation:** Generates creative and engaging job descriptions with a touch of humor.
-   **User-Friendly Interface:** Simple and intuitive Streamlit interface for easy input and output.
-   **Customizable Inputs:** Users can specify role title, seniority, location, and responsibilities.

## Prerequisites

-   Python 3.7+
-   Streamlit (`pip install streamlit`)
-   Google Generative AI library (`pip install google-generativeai`)
-   A Google Gemini API key.

## Setup

1.  **Clone the Repository (Optional):**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install Dependencies:**

    ```bash
    pip install streamlit google-generativeai
    ```

3.  **Set Up Gemini API Key:**

    -   Obtain your Gemini API key from Google AI Studio.
    -   Replace `"AIzaSyBvLxH_CL8nm17Ake-Cr0KMdC8FFYoKmiU"` in the `app.py` file with your actual API key.

    ```python
    GEMINI_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    ```

4.  **Run the Streamlit App:**

    ```bash
    streamlit run app.py
    ```

    This will open the app in your default web browser.

## Usage

1.  **Enter Job Details:**
    -   Enter the role title.
    -   Select the seniority level from the dropdown.
    -   Enter the job location.
    -   Enter the job responsibilities, separated by commas.

2.  **Generate Job Description:**
    -   Click the "Generate Formal JD" button to generate a formal job description.
    -   Click the "Generate Funky JD" button to generate a funky job description.

3.  **View the Job Description:**
    -   The generated job description will be displayed in a text area below the buttons.

## Code Explanation

-   **Streamlit:** Used for creating the web application interface.
-   **Google Generative AI:** Used to interact with the Gemini API and generate the job descriptions.
-   **Regular Expressions (re):** Although included in the import, this version of the code doesn't actively use regular expressions. It was likely included for future text processing functionalities.
-   **CSS Styling:** Custom CSS is embedded in the app to provide a visually appealing interface.

## Notes

-   Ensure your Gemini API key is securely stored and not exposed in public repositories.
-   The quality of the generated job descriptions depends on the clarity and detail of the input provided.
-   The funky job descriptions are generated with a focus on creativity and humor, but the tone may vary.
-   Consider adding error handling and input validation to enhance the robustness of the application.
-   The model used is "models/gemini-1.5-flash-001". You can change this to another available Gemini model.

## Future Enhancements

-   Add more customization options for job descriptions.
-   Implement features to save and export generated job descriptions.
-   Include more advanced text processing and formatting options.
-   Integrate with job posting platforms.
-   Add error handling for API failures.
-   Add input validation.
-   Include regular expression functionality for more robust text processing.
