# aws-s3-alibaba-oss-boto3-test
Test using AWS S3 and Alibaba Cloud OSS with Boto3 in the same way

認証情報は `.aws/credentials` `.aws/config` を使います。

### .aws/credentials

```
[default]
aws_access_key_id = AWSのアクセスキー
aws_secret_access_key = AWSのシークレット

[alibaba]
aws_access_key_id = Alibaba Cloudのアクセスキー
aws_secret_access_key = Alibaba Cloudのシークレット
```

### .aws/config

```
[default]
region = ap-northeast-1

[alibaba]
region　= ap-northeast-1 
```

### BUCKET_NAME_ENVは環境変数を使っています。

```
export BUCKET_NAME_ENV=バケット名
```

個人ブログでの記事用に試したコードです  
[Amazon S3 のSDKで書かれたコードで Alibaba Cloud OSS を操作できるか試してみたよ！](https://blog.matsuda-yoshihiro.com/2021/02/amazon-s3-sdk-alibaba-cloud-oss.html)
