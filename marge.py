import os
import subprocess
import semantic_version
import json
import sys
import time


def create_custom_tag(version_str, base_custom_branch_name, comit_message_script):
	version = semantic_version.Version(version_str, partial=True)
	create_tag = version_str + '-custom'

	subprocess.check_call('git checkout -f origin/{} -B rebase_target'.format(base_custom_branch_name), shell=True)
	subprocess.check_call('git reset --hard HEAD^', shell=True)

	with open('package.json', 'r') as f:
		package_info = json.load(f)
		now_version_str = package_info['version']
		now_version = semantic_version.Version(now_version_str, partial=True)

	subprocess.check_call('git rebase --onto {} {} rebase_target'.format(version_str, now_version_str), shell=True)
	subprocess.check_call('bash ../{}'.format(comit_message_script), shell=True)
	subprocess.check_call('git tag {}'.format(create_tag), shell=True)

	if now_version <= version:
		subprocess.check_call('git branch -f {}'.format(base_custom_branch_name), shell=True)
		subprocess.check_call('git push origin {} --force-with-lease'.format(base_custom_branch_name), shell=True)

	subprocess.check_call('git push origin {}'.format(create_tag), shell=True)

if __name__ == '__main__':
	try:
		os.chdir("./git_tmp")

		with open('package.json', 'r') as f:
			package_info = json.load(f)
			now_version_str = package_info['version']
			now_version = semantic_version.Version(now_version_str, partial=True)

		subprocess.check_call('git config --global user.email "lltcggie@gmail.com"', shell=True)
		subprocess.check_call('git config --global user.name "lltcggie"', shell=True)

		res = subprocess.check_output('git tag', shell=True)
		res = res.decode('utf-8')
		l = res.splitlines()

		all_version_list = [line for line in l if semantic_version.validate(line)]

		release_list = [line for line in all_version_list if (semantic_version.Version(line, partial=True).prerelease == None or semantic_version.Version(line, partial=True).prerelease[0] == 'custom') and not line.endswith('-custom')]
		#prerelease_list = [line for line in all_version_list if (semantic_version.Version(line, partial=True).prerelease != None and semantic_version.Version(line, partial=True).prerelease[0] != 'custom') and not line.endswith('-custom')]
		custom_release_list = [line for line in all_version_list if (semantic_version.Version(line, partial=True).prerelease == None or semantic_version.Version(line, partial=True).prerelease[0] == 'custom') and line.endswith('-custom')]
		#custom_prerelease_list = [line for line in all_version_list if (semantic_version.Version(line, partial=True).prerelease != None and semantic_version.Version(line, partial=True).prerelease[0] != 'custom') and line.endswith('-custom')]

		target_release_list = [line for line in release_list if not line + '-custom' in custom_release_list and semantic_version.Version(line, partial=True) > now_version]
		#target_prerelease_list = [line for line in prerelease_list if not line + '-custom' in custom_prerelease_list and semantic_version.Version(line, partial=True) > now_version]

		target_release_list.sort(key=lambda x:semantic_version.Version(x, partial=True))
		#target_prerelease_list.sort(key=lambda x:semantic_version.Version(x, partial=True))

		is_first = True
		for version_str in target_release_list:
			if not is_first: # for tag push delay
				time.sleep(20)
			create_custom_tag(version_str, 'customize-master', 'comit_message.sh')
			is_first = False

		#is_first = True
		#for version_str in target_prerelease_list:
		#	if not is_first: # for tag push delay
		#		time.sleep(20)
		#	create_custom_tag(version_str, 'customize-release-candidate', 'comit_message.sh')
		#	is_first = False

		#subprocess.check_call('git push origin --tags', shell=True)
	except:
		import traceback
		traceback.print_exc()
		sys.exit(1)
