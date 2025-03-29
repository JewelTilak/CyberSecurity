import streamlit as st

# Define the case studies with detailed descriptions
case_studies = {
    "Phishing Attack": {
        "description": """
        **Phishing Attack on an Analytics Firm in Pune (2025)**

        In February 2025, an analytics firm in Pune, India, fell victim to a whale phishing attack, resulting in a loss of Rs 2.34 crore (approximately $300,000). The attackers posed as the firm's Canada-based Chief Executive Officer (CEO) and manipulated the firm’s accounts officials to transfer large sums of money under the pretext of business transactions.

        **Details:**
        - The attackers called the firm's accounts department, claiming to be the CEO.
        - They requested detailed information about the company's financial deposits.
        - Over the next five days, the firm's accounts staff were manipulated into making 13 transfers, totaling Rs 2.34 crores, to fraudulent mule accounts.
        - The mule accounts were spread across different locations in India, making it difficult to trace the funds.
        - The firm eventually discovered the fraud when a senior director realized that the CEO had not given any such instructions.
        """,
        "question": "You are an accounts manager at the firm. You receive a call from an unidentified number. The caller claims to be the firm’s founder president and CEO and asks you to share details of deposits in all the company accounts. What do you do?",
        "options": [
            "A. Share the details as requested.",
            "B. Verify the caller's identity by calling the CEO's known phone number.",
            "C. Ignore the call and do nothing.",
            "D. Ask the caller to provide more information about the transactions.",
            "E. Report the call to the company's security team."
        ],
        "correct_answers": ["B. Verify the caller's identity by calling the CEO's known phone number.", "D. Ask the caller to provide more information about the transactions.", "E. Report the call to the company's security team."]
    },
    "Malware Attack": {
        "description": """
        **Equifax Data Breach (2017)**

        In 2017, Equifax, a major credit reporting agency in the United States, suffered a massive data breach that exposed the personal information of approximately 147 million consumers. The attackers exploited a vulnerability in the Apache Struts web application framework, which Equifax failed to patch despite the availability of a fix months before the breach.

        **Details:**
        - The attackers gained access to Equifax's systems through a vulnerability in the Apache Struts framework.
        - They were able to move laterally within Equifax’s systems and exfiltrate sensitive information undetected for 76 days.
        - The breach exposed Social Security numbers, birth dates, addresses, and other sensitive information of millions of consumers.
        - Equifax was criticized for not applying the available security patches in a timely manner.
        """,
        "question": "You receive an alert about a potential vulnerability in the Apache Struts framework. What do you do?",
        "options": [
            "A. Ignore the alert because the system has never been compromised before.",
            "B. Investigate the alert and apply the necessary security patches immediately.",
            "C. Wait for the vendor to release an official statement before taking any action.",
            "D. Notify your supervisor and wait for further instructions.",
            "E. Conduct a security audit to identify other potential vulnerabilities."
        ],
        "correct_answers": ["B. Investigate the alert and apply the necessary security patches immediately.", "E. Conduct a security audit to identify other potential vulnerabilities."]
    },
    "DoS Attack": {
        "description": """
        **Mirai Botnet Attack on Dyn (2016)**

        In 2016, the Mirai botnet launched a massive DDoS attack on Dyn, a major DNS provider. The attack caused widespread internet outages, affecting services like Twitter, Netflix, and Reddit. The attackers used a botnet of compromised IoT devices to overwhelm Dyn's servers with traffic.

        **Details:**
        - The Mirai botnet consisted of thousands of compromised IoT devices, such as routers and cameras.
        - The attackers used these devices to send a massive amount of traffic to Dyn's servers, overwhelming them and causing outages.
        - The attack affected major internet services, leading to significant disruptions for users.
        - Dyn had to implement traffic filtering and rate limiting to mitigate the attack.
        """,
        "question": "You notice a sudden increase in traffic that is causing your network to slow down. What do you do?",
        "options": [
            "A. Ignore the increase in traffic as it might be due to high user activity.",
            "B. Investigate the traffic to determine if it is a DDoS attack and take appropriate action.",
            "C. Shut down the network to prevent any potential damage.",
            "D. Notify your supervisor and wait for further instructions.",
            "E. Implement traffic filtering and rate limiting to mitigate the attack."
        ],
        "correct_answers": ["B. Investigate the traffic to determine if it is a DDoS attack and take appropriate action.", "E. Implement traffic filtering and rate limiting to mitigate the attack."]
    },
    "Man-in-the-Middle Attack": {
        "description": """
        **Target Data Breach (2013)**

        In 2013, Target suffered a massive data breach that affected approximately 70 million customers. Attackers gained access to Target's network by compromising a third-party vendor. They used phishing emails to steal the vendor's credentials, which they then used to access Target's systems. Once inside, they installed malware on point-of-sale systems to steal customer credit card information.

        **Details:**
        - The attackers compromised a third-party vendor's credentials through phishing emails.
        - They used these credentials to gain access to Target's network.
        - The attackers installed malware on Target's point-of-sale systems, which allowed them to steal customer credit card information.
        - Target had to implement stronger security measures and improve its incident response capabilities.
        """,
        "question": "You are shopping at a store and notice that the Wi-Fi network seems slow and unsecured. What do you do?",
        "options": [
            "A. Continue shopping and use the Wi-Fi to make online purchases.",
            "B. Avoid using the Wi-Fi and use your mobile data instead.",
            "C. Ask a store employee about the security of the Wi-Fi network.",
            "D. Ignore the issue as it is not your responsibility.",
            "E. Report the issue to the store management."
        ],
        "correct_answers": ["B. Avoid using the Wi-Fi and use your mobile data instead.", "E. Report the issue to the store management."]
    },
    "SQL Injection Attack": {
        "description": """
        **Sony Pictures Hack (2014)**

        In 2014, Sony Pictures suffered a significant data breach that resulted in the theft of sensitive information, including unreleased movies, scripts, and internal communications. Attackers gained access to Sony Pictures' network by exploiting vulnerabilities in the company's systems. They used a combination of malware and social engineering tactics to steal the data.

        **Details:**
        - The attackers exploited vulnerabilities in Sony Pictures' systems to gain unauthorized access.
        - They used malware and social engineering to move laterally within the network and exfiltrate sensitive data.
        - The breach exposed unreleased movies, scripts, and internal communications, causing significant damage to Sony Pictures.
        - Sony Pictures had to improve its security measures and conduct a thorough security audit.
        """,
        "question": "You receive a report about a potential SQL injection vulnerability in the website's login form. What do you do?",
        "options": [
            "A. Ignore the report as it seems insignificant.",
            "B. Investigate the report and fix the vulnerability immediately.",
            "C. Wait for the next scheduled security audit to address the issue.",
            "D. Notify your supervisor and wait for further instructions.",
            "E. Implement input validation and parameterized queries to mitigate the risk."
        ],
        "correct_answers": ["B. Investigate the report and fix the vulnerability immediately.", "E. Implement input validation and parameterized queries to mitigate the risk."]
    },
    "Zero-Day Exploit": {
        "description": """
        **Capital One Data Breach (2019)**

        In 2019, Capital One suffered a data breach that exposed the personal information of over 100 million individuals. The attacker exploited a zero-day vulnerability in a web application firewall (WAF) to gain access to Capital One's AWS environment. The attacker then used the compromised credentials to access sensitive data stored in AWS S3 buckets.

        **Details:**
        - The attacker exploited a zero-day vulnerability in Capital One's web application firewall.
        - They gained access to Capital One's AWS environment and stole sensitive data from S3 buckets.
        - The breach exposed personal information of over 100 million individuals, including Social Security numbers and bank account numbers.
        - Capital One had to implement additional security measures and improve its incident response capabilities.
        """,
        "question": "You receive a notification about a potential zero-day vulnerability in one of your cloud services. What do you do?",
        "options": [
            "A. Ignore the notification as it might be a false alarm.",
            "B. Investigate the notification and apply the necessary security patches immediately.",
            "C. Wait for the vendor to release an official statement before taking any action.",
            "D. Notify your supervisor and wait for further instructions.",
            "E. Implement additional security measures such as multi-factor authentication."
        ],
        "correct_answers": ["B. Investigate the notification and apply the necessary security patches immediately.", "E. Implement additional security measures such as multi-factor authentication."]
    },
    "Ransomware Attack": {
        "description": """
        **Colonial Pipeline Ransomware Attack (2021)**

        In 2021, the Colonial Pipeline, a major fuel pipeline in the United States, suffered a ransomware attack. The attackers used a compromised password to gain access to the company's systems and encrypted critical data, demanding a ransom for the decryption key. The attack caused significant disruptions to fuel supply across the East Coast.

        **Details:**
        - The attackers used a compromised password to gain access to Colonial Pipeline's systems.
        - They encrypted critical data and demanded a ransom for the decryption key.
        - The attack caused significant disruptions to fuel supply, affecting millions of people.
        - Colonial Pipeline had to implement backup and recovery procedures to mitigate the impact.
        """,
        "question": "You receive an alert about a potential ransomware attack on your company's systems. What do you do?",
        "options": [
            "A. Ignore the alert as it might be a false alarm.",
            "B. Investigate the alert and isolate the affected systems immediately.",
            "C. Wait for the vendor to release an official statement before taking any action.",
            "D. Notify your supervisor and wait for further instructions.",
            "E. Implement backup and recovery procedures to mitigate the impact."
        ],
        "correct_answers": ["B. Investigate the alert and isolate the affected systems immediately.", "E. Implement backup and recovery procedures to mitigate the impact."]
    },
    "Insider Threat": {
        "description": """
        **Facebook Insider Threat (2018)**

        In 2018, a former employee of Facebook was charged with stealing proprietary code from the company. The employee had access to the codebase and copied the data to a personal device before leaving the company.

        **Details:**
        - The former employee had access to Facebook's codebase.
        - They copied proprietary code to a personal device before leaving the company.
        - Facebook had to investigate the employee's activities and involve the legal department.
        - The company implemented stricter access controls and data monitoring procedures to prevent future incidents.
        """,
        "question": "You suspect that a former employee might have stolen proprietary information. What do you do?",
        "options": [
            "A. Ignore the suspicion as it might be unfounded.",
            "B. Investigate the employee's access logs and activities before leaving the company.",
            "C. Wait for the employee to return the data voluntarily.",
            "D. Notify your supervisor and involve the legal department.",
            "E. Implement stricter access controls and data monitoring procedures."
        ],
        "correct_answers": ["B. Investigate the employee's access logs and activities before leaving the company.", "D. Notify your supervisor and involve the legal department.", "E. Implement stricter access controls and data monitoring procedures."]
    },
    "Cross-Site Scripting (XSS) Attack": {
        "description": """
        **Social Media Platform XSS Attack (2022)**

        In 2022, a major social media platform suffered an XSS attack. Attackers injected malicious scripts into the platform's web pages, which were then executed by users' browsers, allowing the attackers to steal user data and cookies.

        **Details:**
        - The attackers injected malicious scripts into the platform's web pages.
        - These scripts were executed by users' browsers, allowing the attackers to steal user data and cookies.
        - The platform had to implement input validation and output encoding to mitigate the risk.
        - They also conducted a thorough security audit to identify and fix other potential vulnerabilities.
        """,
        "question": "You receive a report about a potential XSS vulnerability in your company's web application. What do you do?",
        "options": [
            "A. Ignore the report as it seems insignificant.",
            "B. Investigate the report and fix the vulnerability immediately.",
            "C. Wait for the next scheduled security audit to address the issue.",
            "D. Notify your supervisor and wait for further instructions.",
            "E. Implement input validation and output encoding to mitigate the risk."
        ],
        "correct_answers": ["B. Investigate the report and fix the vulnerability immediately.", "E. Implement input validation and output encoding to mitigate the risk."]
    },
    "Business Email Compromise (BEC)": {
        "description": """
        **Manufacturing Company BEC Attack (2023)**

        In 2023, a manufacturing company in Germany fell victim to a BEC attack. Attackers compromised the email account of the company's CFO and sent fraudulent wire transfer requests to the company's financial officers, resulting in significant financial losses.

        **Details:**
        - The attackers compromised the CFO's email account.
        - They sent fraudulent wire transfer requests to the company's financial officers.
        - The company suffered significant financial losses due to the unauthorized transfers.
        - The company had to implement stricter email verification procedures and involve the legal department.
        """,
        "question": "You receive an email from what appears to be your company's CFO, requesting an urgent wire transfer. What do you do?",
        "options": [
            "A. Execute the wire transfer as requested.",
            "B. Verify the request by calling the CFO's known phone number.",
            "C. Ignore the email and do nothing.",
            "D. Notify your supervisor and wait for further instructions.",
            "E. Report the email to the company's security team."
        ],
        "correct_answers": ["B. Verify the request by calling the CFO's known phone number.", "E. Report the email to the company's security team."]
    }
}

# Streamlit app
st.title("Cybersecurity Case Studies Quiz")

# Initialize score
score = 0
total_questions = len(case_studies)

for attack_type, case in case_studies.items():
    st.subheader(attack_type)
    st.write(case["description"])
    st.write(case["question"])
    
    selected_options = []
    for option in case["options"]:
        selected = st.checkbox(option, key=f"{attack_type}_{option}")
        if selected:
            selected_options.append(option)
    
    if st.button("Submit", key=attack_type):
        correct = all(correct in selected_options for correct in case["correct_answers"])
        if correct:
            st.success("Correct! Good job in identifying the appropriate actions.")
            score += 1
        else:
            st.error("Incorrect. The correct answers are: " + ", ".join(case["correct_answers"]))
        st.write(f"Current Score: {score}/{total_questions}")

# Display final score
st.write(f"Final Score: {score}/{total_questions}")
if score == total_questions:
    st.balloons()
    st.success("Congratulations! You answered all questions correctly.")
else:
    st.info("Keep practicing to improve your cybersecurity knowledge.")