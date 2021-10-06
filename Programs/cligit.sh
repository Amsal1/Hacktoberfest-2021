#!/bin/bash
echo "===================CLI BASED GIT================="
echo
echo
echo "1.Configure Git"
echo "2.Git Status"
echo "3.Git Add"
echo "4.Git Commit"
echo "5.Git Push"
echo "6.Git Fetch"
echo "7.Git Pull"
echo "8.Git Branch"
echo "9.Git Create Branch"
echo "10.Git Checkout"
echo "11.Git Merge"
echo "12.Git Clone"
echo "13.Git Remote Add"
echo "14.Git Log"
echo "15.Git Remove"
read op
case $op in
	1)
		echo "Enter User Name"
		read un
		git config --global user.name "${un}"
		echo "Enter Email"
		read em
		git config --global user.email "${em}"
	;;
	2)
		git status
	;;
	3)
		echo
		echo  "1. To Add All File"
		echo  "2. To Add File Specific"
		echo
		read opt
		case $opt in
			1)
			git add .
			;;
			2)
			echo "Enter the File Name"
			read f
			git add "${f}"
			;;
			*)
		esac
	;;
	4)
		echo "Enter the Commit Message"
		read msg
		git commit -m "${msg}"
	;;
	5)
		echo
		echo "1.To Push Into Same Branch"
		echo "2.To Checkout the Branch"
		echo
		read br
		case $br in
			1)
				echo "Enter the Branch Name"
				read bn
				git push origin "${bn}"
			;;
			2)
				echo "Enter the Branch to Checkout"
				read bnc
				git checkout "${bnc}"
				git push origin "${bnc}"
			;;
			*)
		esac
	;;
	6)
		git fetch
	;;
	7)
		git pull
	;;
	8)
		echo "Currently followed (*) by branch name is curent branch"
		git branch
	;;
	9)
		echo "Enter the Branch Name you Want to Create"
		read brnm
		git branch "${brnm}"
	;;
	10)
		echo "Enter the Branch to Checkout"
		read chbr
		git checkout "${chbr}"
	;;
	11)
		echo "Enter the Branch to Merge"
		read brname
		git merge "${brname}"
	;;
	12)
		echo "Enter the link of repo to clone"
		read link
		git clone "${link}"
	;;
	13)
		echo "Enter the Alias And Url"
		read ali
		read url
		git remote add "${ali}" "${url}"
	;;
	14)
		git log
	;;
	15)
		echo "Enter the file name to remove"
		read fname
		git rm -f "${fname}"
	;;
	*)
esac
