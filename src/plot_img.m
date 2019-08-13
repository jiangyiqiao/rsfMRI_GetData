clc;
clear all;

txtDataPath = 'D:\philips_dcm\AD\';
txtDataDir  = dir(txtDataPath);             % 遍历所有文件
for i = 1:length(txtDataDir)
    if(isequal(txtDataDir(i).name,'.')||... % 去除系统自带的两个隐文件夹
       isequal(txtDataDir(i).name,'..')||...
       ~txtDataDir(i).isdir)                % 去除遍历中不是文件夹的
           continue;
    end
    dateDir =dir(strcat(txtDataPath,txtDataDir(i).name,'\Resting_State_fMRI')); 
    for j =1:length(dateDir)                
        if(isequal(dateDir(j).name,'.')||... % 去除系统自带的两个隐文件夹
        isequal(dateDir(j).name,'..')||...
        ~dateDir(j).isdir)                % 去除遍历中不是文件夹的
           continue;
        end
        % 文件存在返回2

        txtDirs = dir(strcat(txtDataPath,txtDataDir(i).name,dateDir( j ).name,'2.NIFTI')); 
        txtpath=fullfile( txtDataPath, txtDataDir(i).name, '\Resting_State_fMRI',dateDir( j ).name,'2.NIFTI','*.txt');
        data = dir( txtpath );               % 子文件夹下找后缀为txt的文件
        for k = 1 : length( data )
            if exist(strcat('D:\philips_dcm\PIC\AD\',txtDataDir(i).name,dateDir( j ).name,data(k).name,'.jpg'),'file')==2
                disp(strcat('D:\philips_dcm\PIC\AD\',txtDataDir(i).name,dateDir( j ).name));
                continue;
            end
            datapath = fullfile(txtDataPath, txtDataDir(i).name, '\Resting_State_fMRI',dateDir( j ).name,'2.NIFTI',data(k).name);
        	disp(datapath);

            [data1,data2,data3,data4,data5,data6]=textread(datapath,'%n%n%n%n%n%n');
            len = size(data1,1);
            data4 = data4*len/pi;
            data5 = data5*len/pi;
            data6 = data6*len/pi;
            
            
        
            x = reshape(linspace(1,len+1,len),1,len);
          
            figure;
            subplot(2,1,1);
            plot(x,data1,x,data2,x,data3);
            title('translation')
            legend('x translation','y translation','z translation')
            grid on;
            subplot(2,1,2);
            plot(x,data4,x,data5,x,data6);
            title('rotation')
            legend('pitch','roll','yaw')
            grid on;


            save_full_path = strcat('D:\philips_dcm\PIC\AD\',txtDataDir(i).name,dateDir( j ).name,data(k).name,'.jpg');
            disp(save_full_path);
            saveas(gcf,save_full_path);
        end
        
    end
end

% for i=1:length(txtFiles)
%     filename = strrep(txtFiles(i),'\','/');
%     disp(filename);
%     [data1,data2,data3,data4,data5,data6]=textread(filename,'%n%n%n%n%n%n');
% 
%     x = linspace(1,188,187);
%     figure;
%     plot(x,data1,x,data2,x,data3);
%     grid on;
% 
%     picName =  strsplit(filename,'.txt');
%     save_full_path = strcat(picName{1,1},'.jpg');
%     disp(save_full_path);
%     saveas(gcf,save_full_path);
% end