clc;
clear all;

% txtDataPath = 'fMRI_37/';
txtDataPath = 'ADNI/';
txtDataDir  = dir(txtDataPath);             % 遍历所有文件
for i = 1:length(txtDataDir)
    if(isequal(txtDataDir(i).name,'.')||... % 去除系统自带的两个隐文件夹
       isequal(txtDataDir(i).name,'..')||...
       ~txtDataDir(i).isdir)                % 去除遍历中不是文件夹的
           continue;
    end
    txtDir =dir(strcat(txtDataPath,txtDataDir(i).name)); 
    for j =1:length(txtDir)                
        if(isequal(txtDir(j).name,'.')||... % 去除系统自带的两个隐文件夹
        isequal(txtDir(j).name,'..')||...
        ~txtDir(j).isdir)                % 去除遍历中不是文件夹的
           continue;
        end
        txtDir( j ).name = strcat(txtDir( j ).name,'\Resting_State_fMRI');
        disp(txtDir( j ).name)
        txtpath=fullfile( txtDataPath, txtDataDir(i).name, txtDir( j ).name,'*.txt');
        data = dir( txtpath );               % 子文件夹下找后缀为txt的文件
        for k = 1 : length( data )
%         for k = 1 : 2  
            datapath = fullfile(txtDataPath, txtDataDir(i).name,  txtDir( j ).name,data(k).name);
        	disp(datapath);
            [data1,data2,data3,data4,data5,data6]=textread(datapath,'%n%n%n%n%n%n');
            data4 = data4*180/pi;
            data5 = data5*180/pi;
            data6 = data6*180/pi;
        
            x = linspace(1,188,187);
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

            picPath = strsplit(datapath,'.txt');
            picName = strsplit(picPath{1,1},'\');
            save_full_path = strcat('fMRI_20_pic\',picName{1,5},'.jpg');
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