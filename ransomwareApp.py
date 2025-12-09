import gradio as gr  # creates the UI 
from pytrends.request import TrendReq  # the Google Trends API
import matplotlib.pyplot as plt  # draws the chart 
import pandas as pd  # fills the chart with data 
from trendsAPI import TrendsAPI  # import my trendsAPI.py
from glossary import UI_Glossary # import my glossary.py 

class RansomwareApp:
    def __init__(self):
        self.api = TrendsAPI()    # every app instance needs the api and example keywords for the dropdown 
        self.region = "US"
        self.example_keywords = [
            "ransomware",
            "malware",
            "ransomware removal",
            "encrypted files",
            "data breach"
        ]
    def get_warning_signs(self):
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
        return "\n".join(f"⚠️ {sign}\n" for sign in signs)

    def get_prevention_tips(self):
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
        return "\n".join(f"✅ {tip}\n" for tip in tips)

    def handle_region_choice(self, region_name):
        self.region = self.api.region_choices.get(region_name, "")
        return f"Region set to: {region_name}"
    
    def analyze_keyword(self, keyword):
        keyword = keyword.strip() # prepare the keyword for a google trends request, return the file and message if successful
        if not keyword:
            return None, "Please enter or click on a keyword."
        plot_path, message = self.api.fetch_google_trends(keyword, self.region) 
        return plot_path, message

    def launch(self): 
        with gr.Blocks() as app:      # this is the wrapper function for the entire UI 
            gr.HTML("""
                    <h1 style='font-size:50px; text-align: center; font-weight:bold;'>Ransomware Awareness</h1>
                    <img src="https://www.radware.com/RadwareSite/MediaLibraries/WordPressImages/uploads/2018/10/origin_of_ransomware_and_business_impacts-960x641.jpg" 
                    style="display:block; width:100%; height:auto; margin:0 auto;">
            """)  
            button1_markdown = gr.Markdown() # markdown outputs text to the screen 
            warning_button = gr.Button("Show Warning Signs")    # button 1
            warning_button.click(fn=self.get_warning_signs, inputs =[], outputs=button1_markdown)    # button 1 trigger 
            region_dropdown = gr.Dropdown(label="Choose a region", choices=self.api.region_choices.keys(), value="U.S.")
            region_output = gr.Markdown() # markdown will print to the screen 
            region_dropdown.change( 
                fn=self.handle_region_choice,
                inputs=[region_dropdown],
                outputs=[region_output])   
            keyword_input = gr.Textbox(label="Enter a keyword")
            keyword_dropdown = gr.Dropdown(label="Or choose an example keyword", choices=self.example_keywords, value=self.example_keywords[0])
            output_plot = gr.Image(label="Trend Chart")
            output_text = gr.Textbox(label="Information")
            keyword_input.submit(        
                fn=self.analyze_keyword,
                inputs=[keyword_input],
                outputs=[output_plot, output_text]
            )  
            keyword_dropdown.change(
                fn=self.analyze_keyword,
                inputs=[keyword_dropdown],
                outputs=[output_plot, output_text]
            )
            button3_markdown = gr.Markdown() 
            prevention_button = gr.Button("Show Prevention Tips") # button 3 
            prevention_button.click(fn=self.get_prevention_tips, inputs =[], outputs=button3_markdown)   # button 3 trigger 
            button4_markdown = gr.Markdown()
            glossary_button = gr.Button("Common Cybersecurity Terms- Glossary")
            glossary_button.click(fn=UI_Glossary().get_glossary, inputs=[], outputs=button4_markdown)   # button 4 trigger 
            gr.Markdown("----------")
            gr.Markdown("Based on guidance from [CISA](https://www.cisa.gov/stopransomware) and [No More Ransom Project](https://www.nomoreransom.org). "
            "\tPlease take the time to explore these websites and share this information with your friends and co-workers.")
        app.launch(share=True)