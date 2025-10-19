from typing import List


class Solution:
	def numUniqueEmails(self, emails: List[str]) -> int:
		unique = set()
		for email in emails:
			local, domain = email.split("@")
			local = local.split("+")[0]
			local = local.replace(".", "")
			normalized = local + "@" + domain
			unique.add(normalized)
		return len(unique)


ss = Solution()
emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(ss.numUniqueEmails(emails))
