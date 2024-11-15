local buf_num = 8   -- :echo nvim_get_current_buff()
vim.api.nvim_buf_set_lines(buf_num, 0, -1, false, {'hello', 'world'})

vim.api.nvim_create_autocm('BufWritePost', {
  group = vim.api.nvim_create_augroup('MarcsCoolNotes', { clear = True })
  callback = function()
    print('wow, we saved a file!')
  end,
})
