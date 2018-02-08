def removeOuterBrakets(sql):
    return sql[1:-1];

def getLastBraketPosition(sql):
    return sql.rfind(')')

def removeSqlComments(sql):
    result = sql
    while result.find('/*') != -1:
        commentStart  = result.find('/*') 
        commentEnd = result.find('*/', commentStart) + 2
        sqlBefore = result[:commentStart]
        sqlAfter = result[commentEnd:]
        result = sqlBefore + sqlAfter

    return result



def getSQLs(sql):
    sql = sql.replace('\t', ' ').replace('\n', '').strip()
    result = []

    # remove outer sqls if any
    if sql[0] == '(':
        sql = removeOuterBrakets(sql).strip()
    
    selectPosition = sql.find('SELECT')
    fromPosition = sql.find('FROM') 
    tablesPosition = fromPosition + 5
    while sql[tablesPosition] == ' ':
        tablesPosition +=1
    
    #inner select
    if sql[tablesPosition] == '(':
        lastbraketPosition = getLastBraketPosition(sql)
        innerSql = sql[tablesPosition:lastbraketPosition]
        result += getSQLs(innerSql)


    colsString = sql[selectPosition + 7 : fromPosition]
    print 'Cols: ' + colsString
    result.append(sql)

    return result



sqlFile = open('query.sql')
sql = sqlFile.read().upper()
sqlFile.close()

sql = removeSqlComments(sql)
sqls = getSQLs(sql)
# for s in sqls:
#     print 'SQL Is: '+ s


