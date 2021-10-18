mysql> desc projects_project;
+-------------+---------------+------+-----+---------+-------+
| Field       | Type          | Null | Key | Default | Extra |
+-------------+---------------+------+-----+---------+-------+
| title       | varchar(200)  | NO   |     | NULL    |       |
| description | longtext      | YES  |     | NULL    |       |
| demo_link   | varchar(2000) | YES  |     | NULL    |       |
| source_link | varchar(2000) | YES  |     | NULL    |       |
| created     | datetime(6)   | NO   |     | NULL    |       |
| id          | char(32)      | NO   | PRI | NULL    |       |
| vote_ratio  | int(11)       | YES  |     | NULL    |       |
| vote_total  | int(11)       | YES  |     | NULL    |       |
+-------------+---------------+------+-----+---------+-------+
8 rows in set (0.00 sec)

mysql> select * from projects_project;
+-----------+-----------------------+-----------+-------------+----------------------------+----------------------------------+------------+------------+
| title     | description           | demo_link | source_link | created                    | id                               | vote_ratio | vote_total |
+-----------+-----------------------+-----------+-------------+----------------------------+----------------------------------+------------+------------+
| Project 1 | Project 1 description | NULL      | NULL        | 2021-10-17 12:39:56.327543 | 13d7d7329a6d4b3eb1bf40c51f1cac86 |         67 |        123 |
| Project 3 | Project 3 description | NULL      | NULL        | 2021-10-17 12:40:47.140889 | 488bbab1457b4e3887bce54e3d01a3c8 |         68 |         24 |
| Project 4 | Project 4 description | NULL      | NULL        | 2021-10-17 12:41:33.200415 | 979fb56014ae497b908246d6ee5f3939 |         88 |        120 |
| Project 5 | Project 5 description | NULL      | NULL        | 2021-10-17 12:42:00.038770 | d9d1a7b2caf5459aabb884b0e52c40c0 |         89 |        234 |
| Project 2 | Project 2 description | NULL      | NULL        | 2021-10-17 12:40:19.666157 | e490873bb23b4182a6d69cacf765d534 |         50 |         34 |
+-----------+-----------------------+-----------+-------------+----------------------------+----------------------------------+------------+------------+
5 rows in set (0.00 sec)


### select title from projects_project;

### DJANGO QUERYSET

In [1]: from projects.models import Project                                                            
                                                                                                       
In [2]: projects = Project.objects.all()                                                               
                                                                                                       
In [3]: print(projects)                                                                                
<QuerySet [
    <Project: Project 1>, 
    <Project: Project 3>, 
    <Project: Project 4>, 
    <Project: Project 5>, 
    <Project: Project 2>]>                                                                                     

### SQL

mysql> select title from projects_project;
+-----------+
| title     |
+-----------+
| Project 1 |
| Project 3 |
| Project 4 |
| Project 5 |
| Project 2 |
+-----------+
5 rows in set (0.00 sec)                                                                                          

### select title from projects_project where title="Project 1";                                                                                           

### DJANGO QUERYSET

In [1]: from projects.models import Project                                                            
                                                                                             
In [2]: obj = Project.objects.get(title="Project 1")                                                   
                                                                                                       
In [3]: print(obj)                                                                                     
Project 1                                                                                              
                                                                                                       
In [4]: print(obj.title)                                                                               
Project 1                                                                                              

### SQL

mysql> select title from projects_project where title="Project 1";
+-----------+
| title     |
+-----------+
| Project 1 |
+-----------+
1 row in set (0.00 sec)


### select created from projects_project where created="2021-10-17 12:39:56.327543";

### DJANGO QUERYSET
                  
In [1]: from projects.models import Project                                                            
                                                                                             
In [2]: obj = Project.objects.get(title="Project 1")                                                   
                                                                                                       
In [3]: print(obj)                                                                                     
Project 1                                                                                              
                                                                                                       
In [4]: print(obj.title)                                                                               
Project 1 

In [5]: print(obj.created)                                                                             
2021-10-17 12:39:56.327543+00:00                                                                       

### SQL

mysql> select created from projects_project where created="2021-10-17 12:39:56.327543";
+----------------------------+
| created                    |
+----------------------------+
| 2021-10-17 12:39:56.327543 |
+----------------------------+
1 row in set (0.00 sec)
                                      
                                                                                                       

### INNER JOIN - projects_project table and projects_review table
###            - OneToMany relationship

### DJANGO QUERYSET
                  
In [1]: from projects.models import Project                                                            
                                                                                             
In [2]: obj = Project.objects.get(title="Project 1")                                                   
                                                                                                       
In [3]: print(obj)                                                                                     
Project 1                                                                                              
                                                                                                       
In [4]: print(obj.title)                                                                               
Project 1 

In [5]: print(obj.created)                                                                             
2021-10-17 12:39:56.327543+00:00 
                                                                                        
In [6]: print(project.review_set.all())                                                               
<QuerySet [<Review: up>]>                                                                              


mysql> SELECT
    -> projects_project.title,
    -> projects_review.value
    -> FROM projects_review
    -> INNER JOIN projects_project ON projects_review.project_id=projects_project.id
    -> WHERE projects_project.title="Project 1";
+-----------+-------+
| title     | value |
+-----------+-------+
| Project 1 | up    |
+-----------+-------+
1 row in set (0.00 sec)


mysql> SELECT
    -> projects_project.title,
    -> projects_review.value
    -> FROM projects_review
    -> INNER JOIN projects_project ON projects_review.project_id=projects_project.id
    -> WHERE projects_project.title="Project 5" OR projects_review.value="up";
+-----------+-------+
| title     | value |
+-----------+-------+
| Project 5 | up    |
| Project 1 | up    |
| Project 3 | up    |
+-----------+-------+
3 rows in set (0.00 sec)


SELECT
projects_project.title,
projects_review.value
FROM projects_review
INNER JOIN projects_project ON projects_review.project_id=projects_project.id
WHERE projects_project.title="Project 5" OR projects_review.value="up";
+-----------+
| title     |
+-----------+
| Project 5 |
| Project 1 |
| Project 3 |
+-----------+
3 rows in set (0.00 sec)


### INNER JOIN - projects_project table and projects_tag table
###            - ManyToMany relationship

### DJANGO QUERYSET
                  
In [1]: from projects.models import Project                                                            
                                                                                             
In [2]: obj = Project.objects.get(title="Project 1")                                                   
                                                                                                       
In [3]: print(obj)                                                                                     
Project 1                                                                                              
                                                                                                       
In [4]: print(obj.title)                                                                               
Project 1 

In [5]: print(obj.created)                                                                             
2021-10-17 12:39:56.327543+00:00 
                                                                                        
In [6]: print(project.review_set.all())                                                               
<QuerySet [<Review: up>]>  
                                                                      
In [7]: print(project.tags.all())                                                                     
<QuerySet [<Tag: Tag 10>, <Tag: Tag 6>]> 


### SQL

### There are 3 tables:

mysql> select * from projects_tag;
+--------+----------------------------+----------------------------------+
| name   | created                    | id                               |
+--------+----------------------------+----------------------------------+
| Tag 1  | 2021-10-17 12:33:49.880686 | 03bbd8ece7cc4b7b8860a6cc65b76826 |
| Tag 3  | 2021-10-17 12:33:58.181618 | 041b202c3cee44e181e419a77955b2db |
| Tag 9  | 2021-10-17 12:34:25.849937 | 13f70470d74f4ccfafeeff42d0d39f13 |
| Tag 4  | 2021-10-17 12:34:02.128582 | 5218cfb3c17d4108bc1c968029a0e0e9 |
| Tag 2  | 2021-10-17 12:33:54.133312 | bac2122274fe4dc79884b5cc63461cf9 |
| Tag 5  | 2021-10-17 12:34:06.561916 | c94dd573f7304763848c43a6884145ad |
| Tag 8  | 2021-10-17 12:34:22.111321 | d6d85179cdcd4bdca8e65427d03917fb |
| Tag 7  | 2021-10-17 12:34:18.046072 | ec377d68e4c947c7a2929c92d9dbfa0e |
| Tag 10 | 2021-10-17 12:34:30.553520 | ee313b7418a5498c9addbcefb80f1121 |
| Tag 6  | 2021-10-17 12:34:13.034582 | efaf38a113c04b11bad33a60b111ceaa |
+--------+----------------------------+----------------------------------+
10 rows in set (0.00 sec)

mysql> select * from projects_project_tags;
+----+----------------------------------+----------------------------------+
| id | project_id                       | tag_id                           |
+----+----------------------------------+----------------------------------+
|  1 | 13d7d7329a6d4b3eb1bf40c51f1cac86 | 03bbd8ece7cc4b7b8860a6cc65b76826 |
|  2 | 13d7d7329a6d4b3eb1bf40c51f1cac86 | 13f70470d74f4ccfafeeff42d0d39f13 |
|  5 | 488bbab1457b4e3887bce54e3d01a3c8 | 5218cfb3c17d4108bc1c968029a0e0e9 |
|  6 | 488bbab1457b4e3887bce54e3d01a3c8 | bac2122274fe4dc79884b5cc63461cf9 |
|  7 | 979fb56014ae497b908246d6ee5f3939 | ee313b7418a5498c9addbcefb80f1121 |
|  8 | 979fb56014ae497b908246d6ee5f3939 | efaf38a113c04b11bad33a60b111ceaa |
| 11 | d9d1a7b2caf5459aabb884b0e52c40c0 | 13f70470d74f4ccfafeeff42d0d39f13 |
| 10 | d9d1a7b2caf5459aabb884b0e52c40c0 | bac2122274fe4dc79884b5cc63461cf9 |
|  9 | d9d1a7b2caf5459aabb884b0e52c40c0 | c94dd573f7304763848c43a6884145ad |
|  3 | e490873bb23b4182a6d69cacf765d534 | 041b202c3cee44e181e419a77955b2db |
|  4 | e490873bb23b4182a6d69cacf765d534 | 5218cfb3c17d4108bc1c968029a0e0e9 |
+----+----------------------------------+----------------------------------+
11 rows in set (0.00 sec)

mysql> select title, description, id, vote_total, vote_ratio from projects_project;
+-----------+-----------------------+----------------------------------+------------+------------+
| title     | description           | id                               | vote_total | vote_ratio |
+-----------+-----------------------+----------------------------------+------------+------------+
| Project 1 | Project 1 description | 13d7d7329a6d4b3eb1bf40c51f1cac86 |        123 |         67 |
| Project 3 | Project 3 description | 488bbab1457b4e3887bce54e3d01a3c8 |         24 |         68 |
| Project 4 | Project 4 description | 979fb56014ae497b908246d6ee5f3939 |        120 |         88 |
| Project 5 | Project 5 description | d9d1a7b2caf5459aabb884b0e52c40c0 |        234 |         89 |
| Project 2 | Project 2 description | e490873bb23b4182a6d69cacf765d534 |         34 |         50 |
+-----------+-----------------------+----------------------------------+------------+------------+
5 rows in set (0.00 sec)

1.projects_tag
2.projects_project_tags
3.projects_project

project     project_tag       tag
Users       UserAddresses     Addresses
=======     =============     =========
Id          Id                Id
FirstName   UserId            City
LastName    AddressId         State
                              Zip
======================================

Users =  projects_project 
Id=id   
UserAddresses =  projects_project_tags  
Id=id, project_id, tag_id
Addresses=projects_tag
Id=id



mysql> SELECT projects_project.*                                                   
    -> FROM  projects_tag                                                          
    -> INNER JOIN                                                                  
    -> projects_project_tags ON projects_tag.id = projects_project_tags.tag_id     
    -> INNER JOIN                                                                  
    -> projects_project ON projects_project_tags.project_id = projects_project.id  
    -> WHERE (projects_tag.id = @tag_id);                                          
Empty set (0.00 sec)                                                               
                                                                                   
mysql> SELECT projects_tag.*                                                       
    -> FROM projects_tag                                                           
    -> INNER JOIN                                                                  
    -> projects_project_tags ON projects_tag.id = projects_project_tags.tag_id     
    -> INNER JOIN                                                                  
    -> projects_project ON projects_project_tags.project_id = projects_project.id  
    -> WHERE (projects_project.id = @project_id);                                  
Empty set (0.00 sec)  


------------------



