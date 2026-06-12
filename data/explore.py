import scanpy as sc
adata = sc.read_h5ad("downloaded_slices/xenium_half.h5ad")
print(adata)