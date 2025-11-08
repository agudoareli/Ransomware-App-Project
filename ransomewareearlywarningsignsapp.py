# An educational app that combines technical warning signs with real-world spikes in public attention.
# gradio website: https://www.gradio.app/guides/sharing-your-app

!pip install gradio --quiet # install the required packages
!pip install pytrends --quiet
import gradio as gr  # UI framework
from pytrends.request import TrendReq  # Google Trends API
import matplotlib.pyplot as plt  # For plotting charts
import pandas as pd  # Data handling
import time  # To apply delays 
from datetime import datetime  # For date/time manipulation

def get_warning_signs():
    signs = [
        "Files suddenly get new strange extensions (e.g., .locked, .crypt).",
        "Unexpected changes to file names or locations.",
        "Large numbers of files being modified or encrypted very quickly.",
        "Backups become inaccessible or are deleted.",
        "System restore settings or snapshots are disabled.",
        "Antivirus or security software gets turned off without your action.",
        "New user accounts appear on your system or network.",
        "**Unusual network traffic or high disk activity when idle.**",
        "Remote Desktop Protocol (RDP) or other remote services exposed to the Internet and being used.",
        "Ransom note pop‑ups or files demanding payment appear on screen."
    ]
    return "\n".join([f"{i+1}. {sign}" for i, sign in enumerate(signs)])

def get_prevention_tips():
    tips = [
        "Keep regular backups: store copies offline or off‑network so ransomware can't reach them.",
        "Update operating systems and applications promptly; apply patches to fix vulnerabilities.",
        "Use strong, unique passwords and enable Multi‑Factor Authentication (MFA) for all critical accounts.",
        "Segment your network and restrict access to sensitive systems; use least privilege and limit RDP exposure.",
        "Never open email attachments or click links from unknown or suspicious senders; enable spam filters.",
        "Use trusted sources for software downloads and avoid unknown USB drives; disable auto‑run for external drives.",
        "Install and maintain antivirus/anti‑malware software and enable application allow‑listing or endpoint detection.",
        "Use a VPN when connecting over public Wi‑Fi and ensure remote access is securely configured.",
        "Do not use high‑privilege accounts for everyday work; restrict administrative rights and manage privileged accounts carefully.",
        "**Report ransomware incidents and do not automatically pay ransom; paying may not restore your data and encourages future attacks.**"
    ]
    return "\n".join([f"{i+1}. {tip}" for i, tip in enumerate(tips)])

class TrendsAPI:
    def __init__(self):
        pass  # no class-level variables necessary

    def fetch_google_trends(self, keyword):
        try:
            pytrends = TrendReq(hl='en-US', tz=360) # sets language and timezone
            pytrends.build_payload([keyword], timeframe='today 12-m') # prepares the request by passing in key-words and timeframe
            time.sleep(1) # pause the program for 1sec to avoid overlaping and crashing
            data = pytrends.interest_over_time()  # fetches the data with the given payload
        except Exception as e:
            return None, f"Error fetching data from Google Trends: {str(e)}"
        if data.empty:
            return None, f"No data available for '{keyword}'. Please try another keyword."
        # Plotting the chart
        plt.figure(figsize=(10, 4))
        plt.plot(data.index, data[keyword], color='blue', label=keyword)
        plt.title(f"Google Trends: {keyword}")
        plt.xlabel("Date")
        plt.ylabel("Search Interest Percentage")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plot_path = "trend_plot.png"
        plt.savefig(plot_path)
        plt.close()
        return plot_path, f"Search Interest Over Time data for '{keyword}'."

class RansomwareApp:
    def __init__(self):
        self.api = TrendsAPI()    # every app instance needs the api and example keywords
        self.example_keywords = [
            "ransomware",
            "malware",
            "ransomware removal",
            "encrypted files",
            "data breach"
        ]

    def analyze_keyword(self, keyword):
        keyword = keyword.strip() # prepare the keyword for a google trends request, return the file and message if successful
        if not keyword:
            return None, "Please enter or click on a keyword."
        plot_path, message = self.api.fetch_google_trends(keyword)
        return plot_path, message

    def launch(self): # launch the app
        intro = (
            "Welcome, this is a Ransomware Early Warning Signs App."
            "\nLearn early warning signs of ransomware, explore Google Trends data, and learn some prevention tips."
        )
        with gr.Blocks(title="Ransomware Awareness App") as app:
            gr.Markdown(intro) # formats the text nicely
            # Tab 1
            with gr.Tab("Warning Signs"):
                gr.Markdown("### Early Warning Signs of Ransomware:") # '###' equals level 3 heading
                gr.Markdown(get_warning_signs())
            # Tab 2
            with gr.Tab("Google Trends Explorer"):
                gr.Markdown("### Explore Google Trends Data")
                keyword_input = gr.Textbox(label="Enter a keyword")
                keyword_dropdown = gr.Dropdown(label="Or choose an example keyword", choices=self.example_keywords, value=self.example_keywords[0])
                output_plot = gr.Image(label="Trend Chart")
                output_text = gr.Textbox(label="Information")
                # Call the functions when the user presses Enter or changes values in the dropdownn
                keyword_input.submit(self.analyze_keyword, inputs=keyword_input, outputs=[output_plot, output_text])  # pass in an input and return a specific output
                keyword_dropdown.change(self.analyze_keyword, inputs=keyword_dropdown, outputs=[output_plot, output_text])
            # Tab 3
            with gr.Tab("Prevention Tips"):
                gr.Markdown("### Prevention Tips:")
                gr.Markdown(get_prevention_tips())
            # List my sources
            gr.Markdown("---")
            gr.Markdown("Based on guidance from [CISA](https://www.cisa.gov/stopransomware) and [No More Ransom Project](https://www.nomoreransom.org).")
            gr.Markdown("Please take the time to explore these websites and share this information with your friends and coworkers.")
        app.launch(share=True)

if __name__ == "__main__":  # only run the file when manaully executed
    app = RansomwareApp()
    app.launch()



