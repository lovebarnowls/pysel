Note: Users on AWS may need to run the following code if they don't have permissions to write files etc:
sudo -i



You are the system administrator for the Anti-Villian League.  You have been tasked with examining and securing a workstation that may have been compromised by a disgruntled employee.

The person who was assigned this workstation (vector) had access to sensitive files, and is suspected of copying those files from the company server and sharing them with unauthorized people. This may include documents, media files or photographs. This person may have also installed spyware or made other changes to compromise the security of the system.

Authorized administrators:

	ubuntu
	stuart
	kevin

Authorized users:

	gru
	phil
	bob
	dave
	norbert
	mike

This workstation is used for web browsing, e-mail and word processing only.  No multimedia files or other applications should be installed.

Company password policy requires that passwords should be complex and of a sufficient length to prevent brute-force attacks.  Passwords on all accounts should be changed on a regular basis, and users should not be able to reuse their recent passwords.  Policies should be implemented to prevent attackers from repeatedly guessing passwords.

The only people who should be able to remotely access the computer are the administrators, and ssh is the only remote access software permitted.
Due to organizational policies, phil, who does not have a security clearence, cannot be granted permission to ssh.
Similarly, Vector will need to use a restricted shell.
sql must be removed for all users.

Bob and Vector would like to form a new group called banana.

Security patches for the operating system and all critical software should be kept up to date.

Auditing should be enable to allow the security team to determine who tries to log into the system.

Critical services: SSH APACHE
