# Ableton Cloud Service

## Description
This Python script automates the process of finding `.als` (Ableton Live Set) files across the computer and uploading them to an AWS S3 bucket. It is designed to run periodically to ensure that all modified files are synchronized to the cloud.

## Features
- [x] Search for `.als` files throughout the entire file system.
- [x] Upload found `.als` files to a specified AWS S3 bucket.
- [x] Use environment variables for AWS credentials and other configurations.
- [ ] **TODO:** Track modifications of `.als` files to only upload changed files.
- [ ] **TODO:** Implement a scheduling mechanism to run the script weekly.
- [ ] **TODO:** Optimize performance for scanning large filesystems.
- [ ] **TODO:** Enhance security measures for file handling and data transmission.

## Setup
1. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the root directory of the project and populate it with the following environment variables:
    ```bash
    AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
    AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
    AWS_S3_BUCKET_NAME=<AWS_S3_BUCKET_NAME>
    ```
    > **Note:** The AWS credentials must have read and write access to the specified S3 bucket.

3. Run the script:
    ```bash     
    python main.py
    ```

## Contributing
Contributions to this project are welcome. Please feel free to fork, modify, and make pull requests or open issues for any improvements or issues encountered.


