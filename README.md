# Does the Quantity of Choices in Experiments Influence Revealed Risk Attitudes?

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the oTree source code for the experimental economics project detailed in the paper, "Does the Quantity of Choices in Experiments Influence Revealed Risk Attitudes?". The experiment investigates how the dimensionality of the choice set systematically influences individuals' revealed risk preferences.

## Abstract

This study examines whether the number of alternatives in experimental choice tasks systematically influences individuals' revealed risk preferences. We conduct an incentivized online experiment with 400 participants recruited via Prolific, comparing behavior in a low-dimensional, binary-choice task (a Holt-and-Laury style Multiple Price List) and a high-dimensional, multi-choice task (the Bomb Risk Elicitation Task). Our findings reveal that participants facing a larger choice set exhibit significantly more risk-seeking behavior. These results challenge the conventional prediction that task complexity uniformly induces risk aversion and demonstrate that choice set dimensionality is a fundamental driver of the "risk elicitation puzzle." The findings carry important implications for experimental design and the interpretation of risk preference estimates.

## Experimental Design

The experiment is programmed using oTree and employs a within-subject design where each participant completes two main tasks in a randomized order to control for learning or fatigue effects.

*   **Task 1: Multi-Choice Task (Bomb Risk Elicitation Task - BRET)**
    This task presents a high-dimensional choice environment. Participants decide how many boxes to open out of 100, where one randomly placed box contains a "bomb." Payoffs increase linearly with the number of opened boxes, but finding the bomb results in zero earnings for the task. This allows for a granular measurement of risk attitudes.

*   **Task 2: Binary-Choice Task (Multiple Price List - MPL)**
    This task presents a low-dimensional choice environment based on the widely used format by Holt and Laury (2002). Participants make ten sequential decisions, each time choosing between a safer lottery (Option A) and a riskier lottery (Option B).

The project also includes a demographics survey and a payment module that randomly selects one of the 11 decisions for real payment.

## Project Structure

This oTree project is organized into several apps:

*   `demographic`: A brief survey to collect participants' demographic information.
*   `binary_1` / `binary_2`: These apps implement the Binary-Choice (MPL) task. The two versions likely correspond to the two experimental sessions with different task orderings.
*   `bret`: Implements the Multi-Choice (Bomb Risk Elicitation Task).
*   `payment`: Calculates the final payoff for each participant based on one randomly selected decision and displays the result.

## Getting Started

To run this project locally, you will need to have Python and oTree installed.

### Prerequisites

*   Python 3.8 or newer
*   oTree 5.x

### Installation & Local Execution

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fengchaoya/risk-elicitation-experiment.git
    cd risk-elicitation-experiment
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    ```bash
    otree resetdb
    ```

5.  **Run the oTree development server:**
    ```bash
    otree devserver
    ```

Once the server is running, you can access the experiment by opening `http://localhost:8000` in your web browser. From the oTree admin interface, you can create a session to test the experiment.

## Citation

If you use the code or findings from this project, please cite the original paper:

Feng, C. (2025). *Does the Quantity of Choices in Experiments Influence Revealed Risk Attitudes?*

## Acknowledgements

The Bomb Risk Elicitation Task (BRET) implementation in the `bret` app is adapted from the original oTree implementation by Felix Holzmeister. We are grateful for his work, which provided a foundation for our multi-choice task.

*   **Original BRET Project:** [felixholzmeister/bret_v5 on GitHub](https://github.com/felixholzmeister/bret_v5)

## Contact

For any questions regarding the code or the research project, please contact Chaoya Feng at chaoyaf@gmail.com.