def checkExisting(itemName, columnName, tableName):
	
	sql = '''
		SELECT CASE WHEN EXISTS (
			SELECT %s 
			FROM %s 
			WHERE '%s' ~ %s
		) 
		THEN CAST(1 AS INT) 
		ELSE CAST(0 AS INT) 
		END;
    ''', (columnName, tableName, itemName, columnName)

	print(sql)
	
def main():

    checkExisting('Northfield', 'city', 'uscitiestop1k')

if __name__ == "__main__":
      
    main()


      # select case when exists (select city from uscitiestop1k Where 'Logan' ~ city) then cast (1 as bit) else cast (0 as bit) end;