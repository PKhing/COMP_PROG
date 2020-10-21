#เนื่องจาก Minimum Edit Distance ใช้เวลานานมากหากเปรียบเทียบสตริงยาวๆ
#เราจึงแบ่งประโยคออกเป็นส่วนๆแทน

real_meme = ["makes a wish on a falling star","smash by a meteor"] 

fake_meme = ["bakes a witch on a falling star","smash bye a mateor"]

## Optional ลองเขียนในรูปแบบของ For loop ดู

def edit_ds_dp(real,fake):
  n = len(real)
  m = len(fake)
  dp = [[0 for j in range(m+1)] for i in range(n+1)]

  for i in range(1,n+1):
    for j in range(1,m+1):
      if real[i-1] == fake[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1+ min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        
  return dp[n][m]

for i in range(len(real_meme)):
  print(real_meme[i]+' VS '+fake_meme[i])
  print('Edit Distance: '+str(edit_ds_dp(real_meme[i],fake_meme[i])))