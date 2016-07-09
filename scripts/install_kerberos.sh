#!/bin/sh

HOSTNAME='kdc.epimine.com'

echo "$HOSTNAME" > /etc/hostname
hostname -b $HOSTNAME

yum install -y krb5-server krb5-workstation pam_krb5

cp kadm5.conf kdc.conf /var/kerberos/krb5kdc
cp krb5.conf /etc

kdb5_util create -s -r EPIMINE.COM
systemctl start krb5kdc kadmin
systemctl enable krb5kdc kadmin

kadmin.local -q "addprinc root/admin"

kadmin.local -q "addprinc -randkey host/$HOSTNAME"
kadmin.local -q "ktadd host/$HOSTNAME"

authconfig --enablekrb5 --update
systemctl reload sshd

