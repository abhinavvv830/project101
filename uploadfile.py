import dropbox,os

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
        
    def upload_file(self,file_from,file_to,local_path,relative_path):
        dbx=dropbox.Dropbox(self.access_token)
        
        for root,dirs,files in os.walk(file_from):
            for name in files:
                print(os.path.join(root,name))
            for name in dirs:
                print(os.path.join(root,name))    
                
                
        relative_path = os.path.relapth(local_path,file_from)
        dropbox_path = os.path.join(file_to,relative_path) 
        
        with open(local_path,"rb") as f:
            dbx.file_upload(f.read(),dropbox_path,mode=WriteMode("overwrite"))
           
def main():
    access_token="sl.BGFDt2lD2deXIEf6Ol3r0CG7vJD__2YnEzU7RkytZfbz-zvNhAiC30CmKOj-lsU-SeUkaU3vsT5rrNj4_0CfWNL-xoZRqJ1unVqN9T8tIHv8-pQUJHz81-JIrucjFT2Z21ZKrSQ" 
    transferData=TransferData(access_token)
     
    file_from="text.txt"
    file_to="/abc/text.txt"
     
    transferData.upload_file(file_from,file_to)
         
if __name__ == "__main__":
    main()   
                    
             
                    